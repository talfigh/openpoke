#!/usr/bin/env python3
"""Baseline eval harness for OpenPoke on the synthetic dataset (no real Gmail, nothing sent).

Run from the repo root with the project venv. Each run writes to evals/baseline/runs/<stamp>_<mode>/
(results.json, summary.md, and the isolated data dir the server used).

    .venv/bin/python evals/run_baseline.py routing    [--sizes 40 100 250 500] [--limit N] [--concurrency 6]
    .venv/bin/python evals/run_baseline.py classifier [--per-bucket 25]
    .venv/bin/python evals/run_baseline.py scenario   [--roster-size 100] [--gmail-latency-ms 600]

Modes
  routing     "Execution Agent Overload". For each roster size, every labeled prompt goes through the real
              Interaction Agent loop (same system prompt, roster rendering and tool schemas). Dispatch is
              stubbed: no execution agent runs and nothing is written, so cases are independent. Scores reuse
              vs duplicate vs misroute, prompt size, latency and cost as the roster grows.
  classifier  Importance watcher precision/recall on a stratified sample of labeled emails.
  scenario    End-to-end replay with the full system on fake Gmail: execution agents, search task,
              triggers, watcher polls with live email deliveries. Checks side effects in the fake outbox.

Requires OPENROUTER_API_KEY (read from .env like the server). Costs real LLM tokens.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import json
import os
import random
import re
import shutil
import statistics
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from contextvars import ContextVar
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES = REPO_ROOT / "evals" / "fixtures" / "synthetic"
RUNS_DIR = REPO_ROOT / "evals" / "baseline" / "runs"
USER_TZ = "America/Toronto"


def _load(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def _prepare_env(run_dir: Path, gmail_latency_ms: int = 0) -> Path:
    """Point the server at an isolated data dir and the fake mailbox. Must run before importing server."""
    data_dir = run_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "timezone.txt").write_text(USER_TZ, encoding="utf-8")
    os.environ["OPENPOKE_DATA_DIR"] = str(data_dir)
    os.environ["OPENPOKE_FAKE_GMAIL"] = str(FIXTURES / "mailbox.json")
    os.environ["OPENPOKE_FAKE_GMAIL_OUTBOX"] = str(data_dir / "fake_gmail_outbox.jsonl")
    os.environ["OPENPOKE_FAKE_GMAIL_LATENCY_MS"] = str(gmail_latency_ms)
    sys.path.insert(0, str(REPO_ROOT))
    return data_dir


# ----------------------------------------------------------------------
# LLM call instrumentation
# ----------------------------------------------------------------------

class LLMMeter:
    """Wraps request_chat_completion everywhere it was imported and records usage per call."""

    def __init__(self) -> None:
        self.calls: List[Dict[str, Any]] = []
        self._tag: ContextVar[str] = ContextVar("llm_tag", default="")
        self.prices: Dict[str, Dict[str, float]] = {}

    def install(self) -> None:
        import server.openrouter_client as oc
        from server.agents.interaction_agent import runtime as ia_runtime
        from server.agents.execution_agent import runtime as ea_runtime
        from server.agents.execution_agent.tasks.search_email import tool as search_tool
        from server.services.gmail import importance_classifier
        from server.services.conversation.summarization import summarizer

        original = oc.request_chat_completion
        meter = self

        def make(caller: str):
            async def wrapped(**kwargs):
                started = time.perf_counter()
                record: Dict[str, Any] = {"caller": caller, "tag": meter._tag.get(), "model": kwargs.get("model")}
                try:
                    response = await original(**kwargs)
                    usage = response.get("usage") or {}
                    record.update(ok=True, prompt_tokens=usage.get("prompt_tokens"), completion_tokens=usage.get("completion_tokens"),
                                  cost=usage.get("cost"))
                    return response
                except Exception as exc:
                    record.update(ok=False, error=str(exc)[:300])
                    raise
                finally:
                    record["latency_s"] = round(time.perf_counter() - started, 3)
                    meter.calls.append(record)
            return wrapped

        ia_runtime.request_chat_completion = make("interaction")
        ea_runtime.request_chat_completion = make("execution")
        search_tool.request_chat_completion = make("search_task")
        importance_classifier.request_chat_completion = make("classifier")
        summarizer.request_chat_completion = make("summarizer")

    async def load_prices(self) -> None:
        import httpx
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                data = (await client.get("https://openrouter.ai/api/v1/models")).json().get("data", [])
            for model in data:
                pricing = model.get("pricing") or {}
                self.prices[model["id"]] = {"prompt": float(pricing.get("prompt") or 0), "completion": float(pricing.get("completion") or 0)}
        except Exception as exc:  # pricing is informational only
            print(f"[warn] could not load OpenRouter pricing: {exc}")

    def cost_of(self, call: Dict[str, Any]) -> Optional[float]:
        if call.get("cost") is not None:
            return float(call["cost"])
        price = self.prices.get(call.get("model") or "")
        if not price or call.get("prompt_tokens") is None:
            return None
        return call["prompt_tokens"] * price["prompt"] + (call.get("completion_tokens") or 0) * price["completion"]

    def summarize(self, calls: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        calls = self.calls if calls is None else calls
        by_caller: Dict[str, Dict[str, Any]] = {}
        for caller in sorted({c["caller"] for c in calls}):
            subset = [c for c in calls if c["caller"] == caller]
            costs = [self.cost_of(c) for c in subset]
            by_caller[caller] = {
                "calls": len(subset),
                "errors": sum(1 for c in subset if not c.get("ok")),
                "prompt_tokens": sum(c.get("prompt_tokens") or 0 for c in subset),
                "completion_tokens": sum(c.get("completion_tokens") or 0 for c in subset),
                "cost_usd": round(sum(c for c in costs if c is not None), 4) if any(c is not None for c in costs) else None,
                "latency_p50_s": _pct([c["latency_s"] for c in subset], 50),
                "latency_p95_s": _pct([c["latency_s"] for c in subset], 95),
            }
        total_cost = [v["cost_usd"] for v in by_caller.values() if v["cost_usd"] is not None]
        return {"calls": len(calls), "cost_usd": round(sum(total_cost), 4) if total_cost else None, "by_caller": by_caller}


def _pct(values: List[float], pct: int) -> Optional[float]:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round(pct / 100 * (len(ordered) - 1))))
    return round(ordered[index], 3)


def _mean(values: List[float]) -> Optional[float]:
    return round(statistics.mean(values), 1) if values else None


# ----------------------------------------------------------------------
# Data dir seeding
# ----------------------------------------------------------------------

def seed_roster(data_dir: Path, names: List[str]) -> None:
    path = data_dir / "execution_agents" / "roster.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(names, indent=2), encoding="utf-8")
    from server.services.execution import get_agent_roster
    get_agent_roster().load()


def seed_agent_logs(names: List[str], topics_by_name: Dict[str, Dict[str, Any]]) -> None:
    """Replace all execution logs with each roster agent's seeded history (what agent search builds profiles from).

    Entries are dated from the topic's start (shifted like the fake mailbox), one day apart, so finished work from
    months ago looks old instead of every agent appearing active today.
    """
    from zoneinfo import ZoneInfo
    from server.services.execution import get_execution_agent_logs
    from server.services.execution.log_store import _encode_payload

    logs = get_execution_agent_logs()
    logs.clear_all()
    anchor = datetime.fromisoformat(_load("mailbox.json")["dataset_now"].replace("Z", "+00:00"))
    shift = timedelta(weeks=round((datetime.now(timezone.utc) - anchor) / timedelta(weeks=1)))
    now, tz = datetime.now(timezone.utc), ZoneInfo(USER_TZ)
    for name in names:
        topic = topics_by_name.get(name)
        if not topic:
            continue
        start = datetime.fromisoformat(topic["start"].replace("Z", "+00:00")) + shift
        lines = []
        for i, item in enumerate(topic["history"]):
            stamp = min(start + timedelta(days=i), now).astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
            lines.append(f'<{item["tag"]} timestamp="{stamp}">{_encode_payload(item["text"])}</{item["tag"]}>\n')
        with logs._log_path(name).open("a", encoding="utf-8") as handle:
            handle.writelines(lines)


def seed_conversation(entries: List[Dict[str, str]]) -> str:
    """Write the seed chat into the conversation log and return the transcript the agent will see."""
    from server.services.conversation import get_conversation_log
    from server.services.conversation.log import _encode_payload

    log = get_conversation_log()
    log.clear()
    with log._path.open("w", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(f'<{entry["tag"]} timestamp="{entry["timestamp"]}">{_encode_payload(entry["text"])}</{entry["tag"]}>\n')
    return log.load_transcript()


def seed_agent_logs_and_triggers(names: List[str], topics_by_name: Dict[str, Dict[str, Any]]) -> int:
    from server.services.execution import get_execution_agent_logs
    from server.services.triggers import get_trigger_service

    logs = get_execution_agent_logs()
    triggers = get_trigger_service()
    created = 0
    for name in names:
        topic = topics_by_name.get(name)
        if not topic:
            continue
        for item in topic["history"]:
            logs._append(name, item["tag"], item["text"])
        trigger = topic.get("trigger")
        if trigger:
            triggers.create_trigger(agent_name=name, payload=trigger["payload"], start_time=trigger["start_time"],
                                    recurrence_rule=trigger.get("recurrence_rule") or None, timezone_name=USER_TZ)
            created += 1
    return created


def _disable_summarization() -> None:
    from server.config import get_settings
    get_settings().conversation_summary_threshold = 0


# ----------------------------------------------------------------------
# Mode: routing (agent overload sweep)
# ----------------------------------------------------------------------

def score_case(case: Dict[str, Any], dispatched: List[str], asked: bool, roster: set[str], answered: bool = False,
               error: Optional[str] = None) -> Dict[str, Any]:
    if error:
        # The LLM call failed (e.g. 402 out of credits); this says nothing about routing quality.
        return {"outcome": "error", "new_agents": [], "existing_agents": [], "forbidden_hit": []}
    gold = case["gold_agents"]
    existing = [n for n in dispatched if n in roster]
    new = [n for n in dispatched if n not in roster]
    case_only = [n for n in new if n.lower() in {r.lower() for r in roster}]
    forbidden_hit = [n for n in dispatched if n in case["forbidden_agents"]]
    expected = case["expected"]

    if not dispatched and not asked and answered and expected != "none":
        # Replied in plain text without delegating (e.g. from conversation history).
        outcome = "answered_from_history" if case.get("answerable_from_history") else "answered_without_agent"
        return {"outcome": outcome, "new_agents": [], "existing_agents": [], "forbidden_hit": []}
    if expected == "none":
        outcome = "correct" if not dispatched else "unneeded_agent"
    elif expected == "multi":
        recall = len(set(gold) & set(dispatched)) / len(gold) if gold else 0.0
        outcome = "correct" if recall >= 0.5 else "asked" if asked and not dispatched else "partial" if recall > 0 else "missed"
        return {"outcome": outcome, "recall": round(recall, 2), "new_agents": new, "existing_agents": existing, "forbidden_hit": forbidden_hit}
    elif expected == "new_agent":
        if existing:
            outcome = "merged_into_existing"
        elif new:
            outcome = "correct"
        else:
            outcome = "asked" if asked else "no_action"
    elif expected in ("ask_user", "ask_user_or_reuse"):
        namesakes = {n for n in roster if case.get("ambiguous_name", "\0").lower() in n.lower()}
        if not dispatched:
            outcome = "correct" if asked else "no_action"
        elif len(set(dispatched)) > 1 and set(dispatched) <= namesakes | set(gold):
            outcome = "correct_fanout"
        elif set(dispatched) <= set(gold):
            outcome = "correct" if expected == "ask_user_or_reuse" else "guessed"
        elif forbidden_hit:
            outcome = "wrong_agent"
        else:
            outcome = "duplicate" if new and not existing else "wrong_agent"
    else:  # reuse
        if gold[0] in dispatched:
            outcome = "correct" if len(set(dispatched)) == 1 else "correct_with_extras"
        elif existing:
            outcome = "wrong_agent"
        elif new:
            outcome = "duplicate"
        else:
            outcome = "asked" if asked else "no_action"
    return {"outcome": outcome, "new_agents": new, "existing_agents": existing, "case_only_mismatch": case_only, "forbidden_hit": forbidden_hit}


CORRECT = {"correct", "correct_with_extras", "correct_fanout", "answered_from_history"}


_EMPTY_CAPTURE = {"agents": [], "user_messages": [], "waits": [], "drafts": []}
_SHOWN_AGENT_RE = re.compile(r'<agent name="([^"]*)"')


class DispatchStubs:
    """Replace the interaction agent's side-effecting tools with recorders (no agent runs, nothing written).

    Tools are called synchronously inside each case's own task, so captures are keyed by asyncio task.
    """

    def __init__(self) -> None:
        from server.agents.interaction_agent import tools as ia_tools
        from server.services.execution import get_agent_roster

        self.captures: Dict[int, Dict[str, Any]] = {}
        ToolResult = ia_tools.ToolResult

        def cap() -> Dict[str, Any]:
            return self.captures.setdefault(id(asyncio.current_task()), {k: [] for k in _EMPTY_CAPTURE})

        def send_message_to_agent(agent_name: str, instructions: str):
            cap()["agents"].append({"agent_name": agent_name, "instructions": instructions})
            return ToolResult(success=True, payload={"status": "submitted", "agent_name": agent_name,
                                                     "new_agent_created": agent_name not in get_agent_roster().get_agents()})

        def send_message_to_user(message: str):
            cap()["user_messages"].append(message)
            return ToolResult(success=True, payload={"status": "delivered"}, user_message=message, recorded_reply=True)

        def send_draft(to: str, subject: str, body: str):
            cap()["drafts"].append({"to": to, "subject": subject})
            return ToolResult(success=True, payload={"status": "draft_recorded", "to": to, "subject": subject}, recorded_reply=True)

        def wait(reason: str):
            cap()["waits"].append(reason)
            return ToolResult(success=True, payload={"status": "waiting", "reason": reason}, recorded_reply=True)

        ia_tools.send_message_to_agent, ia_tools.send_message_to_user = send_message_to_agent, send_message_to_user
        ia_tools.send_draft, ia_tools.wait = send_draft, wait

    async def route(self, runtime, system_prompt: str, transcript: str, prompt: str, tag: str, meter: "LLMMeter") -> Dict[str, Any]:
        """Run one user message through the real interaction loop and return what it tried to do."""
        from server.agents.interaction_agent.agent import prepare_message_with_history

        started = time.perf_counter()
        task_key = None
        error = final_text = iterations = None
        shown: List[str] = []

        async def body():
            nonlocal task_key
            task_key = id(asyncio.current_task())
            meter._tag.set(tag)
            messages = prepare_message_with_history(prompt, transcript, message_type="user")
            shown.extend(html.unescape(n) for n in _SHOWN_AGENT_RE.findall(messages[0]["content"]))
            return await runtime._run_interaction_loop(system_prompt, messages)

        try:
            summary = await asyncio.wait_for(asyncio.create_task(body()), timeout=180)
            iterations, final_text = len(summary.tool_names), summary.last_assistant_text
        except Exception as exc:
            error = str(exc)[:300]
        cap = self.captures.pop(task_key, {k: [] for k in _EMPTY_CAPTURE})
        first = next((c for c in meter.calls if c["tag"] == tag), {})
        return {**cap, "shown_agents": shown, "final_text": final_text, "error": error, "tool_calls": iterations,
                "latency_s": round(time.perf_counter() - started, 2), "first_call_prompt_tokens": first.get("prompt_tokens")}


def _mentions_person(prompt: str, people: List[str], agent_name: str) -> bool:
    """Same rule as the generator: does the agent name contain a name token the prompt actually uses?"""
    words = {w.lower().removesuffix("'s") for w in prompt.replace("?", " ").split()}
    used = {tok.lower() for person in people for tok in person.split() if tok.lower() in words and len(tok) > 2}
    return any(tok in agent_name.lower() for tok in used)


def build_rosters(source: str) -> Tuple[Dict[str, List[str]], Dict[str, str]]:
    """Rosters per size and a map from generator agent name -> agent name in this roster source."""
    rosters = _load("rosters.json")["rosters"]
    if source == "synthetic":
        return rosters, {n: n for names in rosters.values() for n in names}
    organic = json.loads((FIXTURES / "organic_roster.json").read_text(encoding="utf-8"))
    topics = {t["id"]: t for t in _load("topics.json")["topics"]}
    name_map = {topics[tid]["agent_name"]: rec["agent_name"] for tid, rec in organic["topics"].items() if rec.get("agent_name")}
    out: Dict[str, List[str]] = {}
    for size, names in rosters.items():
        seen: Dict[str, None] = {}
        for n in names:
            mapped = name_map.get(n)
            if mapped:
                seen.setdefault(mapped, None)
        out[size] = list(seen)
    return out, name_map


def expand_cases(cases: List[Dict[str, Any]], prompts: str, name_map: Dict[str, str], source: str) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Translate gold/forbidden names into the roster source and add paraphrase variants."""
    topic_people = {t["agent_name"]: t["people"] for t in _load("topics.json")["topics"]}
    variants = _load("prompt_variants.json").get("paraphrases", {}) if prompts != "original" else {}
    out, skipped = [], []
    for case in cases:
        gold = [name_map[g] for g in case["gold_agents"] if g in name_map]
        if case["expected"] in ("reuse",) and not gold:
            skipped.append(case["id"])  # the organic run never created an agent for this topic
            continue
        forbidden = [name_map[f] for f in case["forbidden_agents"] if f in name_map and name_map[f] not in gold]
        texts = ([(0, case["prompt"])] if prompts in ("original", "all") else []) + \
                [(i + 1, t) for i, t in enumerate(variants.get(case["id"], []))]
        for variant, text in texts:
            c = {**case, "id": case["id"] if variant == 0 else f"{case['id']}.p{variant}", "base_id": case["id"], "variant": variant,
                 "prompt": text, "gold_agents": list(dict.fromkeys(gold)), "forbidden_agents": forbidden}
            if case["expected"] == "reuse":
                c["name_mentions_person"] = _mentions_person(text, topic_people.get(case["gold_agents"][0], []), gold[0])
            out.append(c)
    return out, skipped


async def run_routing(args, run_dir: Path, meter: LLMMeter) -> Dict[str, Any]:
    from server.agents.interaction_agent.agent import build_system_prompt
    from server.agents.interaction_agent.runtime import InteractionAgentRuntime

    _disable_summarization()
    rosters, name_map = build_rosters(args.roster)
    cases = _load("routing_cases.json")["cases"]
    if args.kinds:
        cases = [c for c in cases if c["kind"] in args.kinds]
    if args.limit:
        rng = random.Random(0)
        cases = sorted(rng.sample(cases, min(args.limit, len(cases))), key=lambda c: c["id"])
    cases, skipped = expand_cases(cases, args.prompts, name_map, args.roster)
    if skipped:
        print(f"skipping {len(skipped)} cases whose topic has no agent in the {args.roster} roster: {skipped}")
    transcript = seed_conversation(_load("conversation_seed.json")["entries"])
    stubs = DispatchStubs()
    runtime = InteractionAgentRuntime()
    system_prompt = build_system_prompt()
    results: List[Dict[str, Any]] = []
    sem = asyncio.Semaphore(args.concurrency)

    seeded_topics = {name_map.get(t["agent_name"], t["agent_name"]): t for t in reversed(_load("topics.json")["topics"])}
    for size in args.sizes:
        names = rosters[str(size)]
        seed_roster(run_dir / "data", names)
        seed_agent_logs(names, seeded_topics)
        if args.agent_roster == "search":
            from server.services.execution.agent_index import get_agent_index
            get_agent_index().warm_up()  # embed every profile before cases start, like server startup
        roster_set = set(names)
        print(f"\n== roster size {size} ({len(names)} agents, {args.roster} names): {len(cases)} cases")

        async def run_case(case: Dict[str, Any]) -> None:
            async with sem:
                out = await stubs.route(runtime, system_prompt, transcript, case["prompt"], f"{size}:{case['id']}", meter)
                dispatched = [a["agent_name"] for a in out["agents"]]
                score = score_case(case, dispatched, bool(out["user_messages"]), roster_set, answered=bool(out["final_text"]), error=out["error"])
                results.append({
                    "roster_size": size, "case_id": case["id"], "base_id": case["base_id"], "variant": case["variant"], "kind": case["kind"],
                    "prompt": case["prompt"], "expected": case["expected"], "gold_agents": case["gold_agents"],
                    "forbidden_agents": case["forbidden_agents"], "name_mentions_person": case.get("name_mentions_person"),
                    "dispatched": out["agents"], "user_messages": out["user_messages"], "waits": out["waits"], "final_text": out["final_text"],
                    "error": out["error"], "latency_s": out["latency_s"], "tool_calls": out["tool_calls"],
                    "first_call_prompt_tokens": out["first_call_prompt_tokens"], "shown_agents": out["shown_agents"], **score,
                })
                mark = "ok " if score["outcome"] in CORRECT else "XX "
                print(f"  {mark}{case['id']:<8} {case['kind']:<9} {score['outcome']:<22} {out['latency_s']:5.1f}s  {case['prompt'][:55]!r} -> {dispatched[:2]}")

        await asyncio.gather(*(run_case(c) for c in cases))
        failed = sum(1 for r in results if r["roster_size"] == size and r["outcome"] == "error")
        if failed > 0.05 * len(cases):
            print(f"\n!! {failed}/{len(cases)} cases failed at roster {size} (first error: "
                  f"{next(r['error'] for r in results if r['outcome'] == 'error')[:160]}). Stopping the sweep.")
            args.sizes = [x for x in args.sizes if x <= size]
            break

    report = aggregate_routing(results, args.sizes, meter)
    report["rosters_used"] = {str(size): rosters[str(size)] for size in args.sizes}
    report["skipped_cases"] = skipped
    return report


async def run_grow_roster(args, run_dir: Path, meter: LLMMeter) -> Dict[str, Any]:
    """Let OpenPoke name its own agents: hand it each topic's first request, in creation order, as the roster grows."""
    from server.agents.interaction_agent.agent import build_system_prompt
    from server.agents.interaction_agent.runtime import InteractionAgentRuntime

    _disable_summarization()
    topics_by_name = {t["agent_name"]: t for t in _load("topics.json")["topics"]}
    order = _load("rosters.json")["rosters"][str(max(_load("rosters.json")["sizes"]))]
    if args.limit:
        order = order[: args.limit]
    requests = _load("prompt_variants.json")["creation_requests"]
    transcript = seed_conversation(_load("conversation_seed.json")["entries"])
    stubs = DispatchStubs()
    runtime = InteractionAgentRuntime()
    system_prompt = build_system_prompt()

    names: List[str] = []
    records: Dict[str, Dict[str, Any]] = {}
    owner: Dict[str, str] = {}  # agent name -> first topic id that created it
    for i, my_name in enumerate(order):
        topic = topics_by_name[my_name]
        seed_roster(run_dir / "data", names)
        out = await stubs.route(runtime, system_prompt, transcript, requests[topic["id"]], f"grow:{topic['id']}", meter)
        dispatched = [a["agent_name"] for a in out["agents"]]
        new = [n for n in dict.fromkeys(dispatched) if n not in names]
        chosen = new[0] if new else (dispatched[0] if dispatched else None)
        for n in new:
            names.append(n)
            owner.setdefault(n, topic["id"])
        records[topic["id"]] = {
            "generator_name": my_name, "agent_name": chosen, "created_new": bool(new), "reused_existing": bool(dispatched) and not new,
            "reused_owner_topic": owner.get(chosen) if dispatched and not new else None, "all_dispatched": dispatched,
            "asked_user": out["user_messages"][:1] if not dispatched else [], "request": requests[topic["id"]], "error": out["error"],
        }
        status = "new " if new else "REUSED" if dispatched else "NONE"
        print(f"  [{i + 1:3d}/{len(order)}] {status:<6} {chosen!r:<55} <- {my_name!r}")
        if (i + 1) % 25 == 0 or i + 1 == len(order):
            payload = {"model": runtime.model, "created_at": datetime.now(timezone.utc).isoformat(), "order": names, "topics": records}
            (run_dir / "organic_roster.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    shutil.copy(run_dir / "organic_roster.json", FIXTURES / "organic_roster.json")
    return {"names": name_comparison(records), "llm": meter.summarize()}


def aggregate_routing(results: List[Dict[str, Any]], sizes: List[int], meter: "LLMMeter") -> Dict[str, Any]:
    per_size: Dict[str, Any] = {}
    for size in sizes:
        all_rows = [r for r in results if r["roster_size"] == size]
        rows = [r for r in all_rows if r["outcome"] != "error"]
        outcomes = Counter(r["outcome"] for r in rows)
        by_kind = {}
        for kind in sorted({r["kind"] for r in rows}):
            k_rows = [r for r in rows if r["kind"] == kind]
            by_kind[kind] = {"n": len(k_rows), "accuracy": round(sum(r["outcome"] in CORRECT for r in k_rows) / len(k_rows), 3),
                             "outcomes": dict(Counter(r["outcome"] for r in k_rows))}
        reuse_rows = [r for r in rows if r["expected"] == "reuse"]
        per_size[str(size)] = {
            "cases": len(rows),
            "errored_cases_excluded": len(all_rows) - len(rows),
            "accuracy": round(sum(r["outcome"] in CORRECT for r in rows) / len(rows), 3) if rows else None,
            "reuse_accuracy": round(sum(r["outcome"] in CORRECT for r in reuse_rows) / len(reuse_rows), 3) if reuse_rows else None,
            "duplicate_rate_on_reuse": round(sum(r["outcome"] == "duplicate" for r in reuse_rows) / len(reuse_rows), 3) if reuse_rows else None,
            "misroute_rate_on_reuse": round(sum(r["outcome"] == "wrong_agent" for r in reuse_rows) / len(reuse_rows), 3) if reuse_rows else None,
            "new_task_merged_rate": _rate(rows, "new", "merged_into_existing"),
            "reuse_accuracy_name_mentions_person": _acc([r for r in reuse_rows if r.get("name_mentions_person") is True]),
            "reuse_accuracy_name_opaque": _acc([r for r in reuse_rows if r.get("name_mentions_person") is False]),
            "case_only_name_mismatches": sum(bool(r.get("case_only_mismatch")) for r in rows),
            "errors": len(all_rows) - len(rows),
            "first_call_prompt_tokens_mean": _mean([r["first_call_prompt_tokens"] for r in rows if r["first_call_prompt_tokens"]]),
            "latency_p50_s": _pct([r["latency_s"] for r in rows], 50),
            "latency_p95_s": _pct([r["latency_s"] for r in rows], 95),
            "llm": meter.summarize([c for c in meter.calls if c["tag"].startswith(f"{size}:")]),
            "gold_shown_on_reuse": round(sum(1 for r in reuse_rows if r.get("shown_agents") and r["gold_agents"][0] in r["shown_agents"])
                                         / len(reuse_rows), 3) if reuse_rows and any(r.get("shown_agents") for r in reuse_rows) else None,
            "accuracy_original_prompts": _acc([r for r in rows if not r.get("variant")]),
            "accuracy_paraphrased_prompts": _acc([r for r in rows if r.get("variant")]),
            "outcomes": dict(outcomes),
            "by_kind": by_kind,
        }
    return {"per_size": per_size, "cases": results}


def _acc(rows: List[Dict[str, Any]]) -> Optional[float]:
    return round(sum(r["outcome"] in CORRECT for r in rows) / len(rows), 3) if rows else None


def _rate(rows: List[Dict[str, Any]], kind: str, outcome: str) -> Optional[float]:
    subset = [r for r in rows if r["kind"] == kind]
    return round(sum(r["outcome"] == outcome for r in subset) / len(subset), 3) if subset else None


def rescore_routing(path: Path) -> None:
    report = json.loads(path.read_text(encoding="utf-8"))
    cases = {c["id"]: c for c in _load("routing_cases.json")["cases"]}
    rosters = _load("rosters.json")["rosters"]
    rows = report["results"]["cases"]
    used = report["results"].get("rosters_used") or rosters
    for row in rows:
        case = {**cases[row.get("base_id", row["case_id"])], **{k: row[k] for k in ("gold_agents", "forbidden_agents") if k in row}}
        dispatched = [a["agent_name"] for a in row["dispatched"]]
        # Older runs didn't store final_text: no tool calls and no error means the model replied in plain text.
        answered = bool(row.get("final_text")) or (row.get("tool_calls") == 0 and not row.get("error"))
        row.update(score_case(case, dispatched, bool(row["user_messages"]), set(used[str(row["roster_size"])]), answered=answered, error=row.get("error")))
        if "base_id" not in row:
            row["name_mentions_person"] = case.get("name_mentions_person")
    meter = LLMMeter()
    meter.calls = []
    old = report["results"]["per_size"]
    keep = {k: report["results"][k] for k in ("rosters_used", "skipped_cases") if k in report["results"]}
    report["results"] = {**aggregate_routing(rows, [int(s) for s in old], meter), **keep}
    for size, stats in report["results"]["per_size"].items():
        stats["llm"] = old[size]["llm"]  # usage isn't stored per call in results.json; keep the original totals
    report["rescored_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(report, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    summary = path.parent / "summary.md"
    header = summary.read_text(encoding="utf-8").split("\n\n", 2)[:2] if summary.exists() else ["# routing", ""]
    summary.write_text("\n\n".join(header) + "\n\n" + routing_markdown(report) + "\n", encoding="utf-8")
    write_failures(path)
    print(routing_markdown(report).split("Failures")[0])


_STOP = {"the", "and", "for", "with", "to", "of", "a", "re", "ltd", "inc", "co"}


def _tokens(name: str) -> set:
    import re
    return {t for t in re.findall(r"[a-z0-9]+", name.lower()) if t not in _STOP}


def _slug(name: str) -> str:
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in name.strip()).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug


def _near_duplicates(names: List[str], threshold: float = 0.6) -> List[Tuple[str, str]]:
    toks = [(n, _tokens(n)) for n in names]
    pairs = []
    for i in range(len(toks)):
        for j in range(i + 1, len(toks)):
            a, b = toks[i][1], toks[j][1]
            if a and b and len(a & b) / len(a | b) >= threshold:
                pairs.append((toks[i][0], toks[j][0]))
    return pairs


def name_comparison(records: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Compare OpenPoke's own agent names with the generator's names for the same topics."""
    topics = {t["id"]: t for t in _load("topics.json")["topics"]}
    rows = []
    for tid, rec in records.items():
        t = topics[tid]
        person_tokens = {tok.lower() for p in t["people"] for tok in p.split() if len(tok) > 2}
        company = t["client"] if t["client"] and t["client"] not in t["people"] else ""
        company_token = company.split()[0].lower() if company else ""
        def info(name):
            n = (name or "").lower()
            return {"person": any(tok in n for tok in person_tokens), "company": bool(company_token) and company_token in n,
                    "words": len((name or "").split())}
        rows.append({"topic": tid, "kind": t["kind"], "mine": rec["generator_name"], "openpoke": rec["agent_name"],
                     "has_people": bool(person_tokens), "has_company": bool(company), "mine_info": info(rec["generator_name"]),
                     "op_info": info(rec["agent_name"]), "reused": rec["reused_existing"], "created": rec["created_new"],
                     "owner": rec.get("reused_owner_topic")})
    created = [r for r in rows if r["created"]]
    reused = [r for r in rows if r["reused"]]
    none = [r for r in rows if not r["created"] and not r["reused"]]
    people_rows = [r for r in rows if r["has_people"] and r["openpoke"]]
    company_rows = [r for r in rows if r["has_company"] and r["openpoke"]]

    def same_people(r):
        if not r["owner"]:
            return False
        return bool(set(topics[r["topic"]]["people"]) & set(topics[r["owner"]]["people"]))

    op_names = list(dict.fromkeys(r["openpoke"] for r in rows if r["openpoke"]))
    my_names = [r["mine"] for r in rows]
    slug_groups = defaultdict(list)
    for n in op_names:
        slug_groups[_slug(n)].append(n)
    rng = random.Random(5)
    return {
        "topics": len(rows), "agents_created": len(op_names), "created_new": len(created), "reused_existing_at_creation": len(reused),
        "no_agent": len(none),
        "reused_same_person": sum(same_people(r) for r in reused), "reused_unrelated": sum(not same_people(r) for r in reused),
        "identical_to_generator": sum(1 for r in rows if r["openpoke"] == r["mine"]),
        "mentions_person": {"generator": _ratio([r["mine_info"]["person"] for r in people_rows]), "openpoke": _ratio([r["op_info"]["person"] for r in people_rows])},
        "mentions_company": {"generator": _ratio([r["mine_info"]["company"] for r in company_rows]), "openpoke": _ratio([r["op_info"]["company"] for r in company_rows])},
        "mean_words": {"generator": _mean([r["mine_info"]["words"] for r in rows]), "openpoke": _mean([r["op_info"]["words"] for r in rows if r["openpoke"]])},
        "near_duplicate_pairs": {"generator": len(_near_duplicates(my_names)), "openpoke": len(_near_duplicates(op_names))},
        "near_duplicate_examples": _near_duplicates(op_names)[:15],
        "case_or_punctuation_collisions": [g for g in slug_groups.values() if len(g) > 1],
        "reused_examples": [{"request": records[r["topic"]]["request"], "went_to": r["openpoke"], "generator_name": r["mine"], "same_person": same_people(r)} for r in reused[:25]],
        "no_agent_examples": [{"request": records[r["topic"]]["request"], "reply": records[r["topic"]]["asked_user"]} for r in none[:10]],
        "sample": [{"generator": r["mine"], "openpoke": r["openpoke"]} for r in rng.sample(rows, min(30, len(rows)))],
    }


def _ratio(flags: List[bool]) -> Optional[float]:
    return round(sum(flags) / len(flags), 3) if flags else None


def names_markdown(report: Dict[str, Any]) -> str:
    n = report["results"]["names"]
    lines = [f"- Topics handed to OpenPoke in creation order: {n['topics']}",
             f"- Distinct agents it created: {n['agents_created']} · topics put into an already existing agent: {n['reused_existing_at_creation']} "
             f"({n['reused_same_person']} same person, {n['reused_unrelated']} unrelated) · no agent at all: {n['no_agent']}",
             f"- Names identical to the generator's: {n['identical_to_generator']}", "",
             "| | Generator names | OpenPoke names |", "|---|---|---|",
             f"| Name mentions the person | {_fmt(n['mentions_person']['generator'])} | {_fmt(n['mentions_person']['openpoke'])} |",
             f"| Name mentions the company (commercial clients) | {_fmt(n['mentions_company']['generator'])} | {_fmt(n['mentions_company']['openpoke'])} |",
             f"| Mean words per name | {n['mean_words']['generator']} | {n['mean_words']['openpoke']} |",
             f"| Near-duplicate name pairs (token overlap ≥ 60%) | {n['near_duplicate_pairs']['generator']} | {n['near_duplicate_pairs']['openpoke']} |",
             f"| Names that collide on the log-file slug (NOTES 3.3) | 0 | {len(n['case_or_punctuation_collisions'])} |",
             f"| LLM cost | | ${report['results']['llm']['cost_usd']} |", "",
             "Side by side (random sample):", "", "| Generator | OpenPoke |", "|---|---|"]
    lines += [f"| {x['generator']} | {x['openpoke']} |" for x in n["sample"]]
    lines += ["", "New work put into an existing agent at creation time:", ""]
    lines += [f"- {'same person' if x['same_person'] else '**unrelated**'}: \"{x['request'][:110]}\" → {x['went_to']} (should be new: {x['generator_name']})" for x in n["reused_examples"]]
    lines += ["", "Near-duplicate OpenPoke names:", ""] + [f"- {a} ≈ {b}" for a, b in n["near_duplicate_examples"]]
    if n["case_or_punctuation_collisions"]:
        lines += ["", "Slug collisions (two roster entries, one log file):", ""] + [f"- {' / '.join(g)}" for g in n["case_or_punctuation_collisions"]]
    if n["no_agent_examples"]:
        lines += ["", "No agent created:", ""] + [f"- \"{x['request'][:100]}\" → {(x['reply'] or ['(plain reply)'])[0][:100]}" for x in n["no_agent_examples"]]
    return "\n".join(lines)


def _spread(values: List[Optional[float]], pct: bool = True) -> str:
    vals = [v for v in values if v is not None]
    if not vals:
        return "-"
    fmt = (lambda v: f"{v:.0%}") if pct else (lambda v: f"{v:,.0f}" if abs(v) >= 100 else f"{v:.2f}")
    if len(vals) == 1:
        return fmt(vals[0])
    return f"{fmt(statistics.mean(vals))} ({fmt(min(vals))}–{fmt(max(vals))})"


def compare_runs(run_dirs: List[Path]) -> str:
    reports = [json.loads((d / "results.json").read_text(encoding="utf-8")) for d in run_dirs]
    modes = {r["mode"] for r in reports}
    if len(modes) != 1:
        sys.exit(f"compare needs runs of one mode, got {sorted(modes)}")
    mode = modes.pop()
    lines = [f"# {mode}: {len(reports)} runs", "", "Runs: " + ", ".join(d.name for d in run_dirs), "",
             "Each cell is mean (min–max) across runs.", ""]
    if mode == "routing":
        sizes = list(reports[0]["results"]["per_size"])
        metrics = [("Accuracy", "accuracy", True), ("Reuse accuracy", "reuse_accuracy", True),
                   ("Duplicate on reuse", "duplicate_rate_on_reuse", True), ("Misroute on reuse", "misroute_rate_on_reuse", True),
                   ("New job merged", "new_task_merged_rate", True), ("Reuse, name mentions person", "reuse_accuracy_name_mentions_person", True),
                   ("Reuse, name opaque", "reuse_accuracy_name_opaque", True), ("Prompt tokens (1st call)", "first_call_prompt_tokens_mean", False),
                   ("Latency p50 s", "latency_p50_s", False)]
        lines += ["| Metric | " + " | ".join(sizes) + " |", "|---|" + "---|" * len(sizes)]
        for label, key, pct in metrics:
            lines.append(f"| {label} | " + " | ".join(_spread([r["results"]["per_size"][s].get(key) for r in reports], pct) for s in sizes) + " |")
        lines.append("| Cost $ | " + " | ".join(_spread([r["results"]["per_size"][s]["llm"]["cost_usd"] for r in reports], False) for s in sizes) + " |")
        kinds = sorted({k for r in reports for s in sizes for k in r["results"]["per_size"][s]["by_kind"]})
        lines += ["", "Accuracy by case kind:", "", "| Kind | " + " | ".join(sizes) + " |", "|---|" + "---|" * len(sizes)]
        for kind in kinds:
            lines.append(f"| {kind} | " + " | ".join(_spread([r["results"]["per_size"][s]["by_kind"].get(kind, {}).get("accuracy") for r in reports]) for s in sizes) + " |")
        # Per-case stability: how often each case is correct across runs at the largest and smallest size.
        for s in (sizes[0], sizes[-1]):
            flips = defaultdict(list)
            for r in reports:
                for c in r["results"]["cases"]:
                    if str(c["roster_size"]) == s:
                        flips[c["case_id"]].append(c["outcome"] in CORRECT)
            unstable = sum(1 for v in flips.values() if len(set(v)) > 1)
            lines.append(f"\nRoster {s}: {unstable} of {len(flips)} cases changed outcome between runs.")
    elif mode == "classifier":
        lines += ["| Metric | Value |", "|---|---|"]
        for label, key in [("High-importance recall", "high_recall"), ("Low-importance false positives", "low_false_positive_rate"),
                           ("Medium surfaced", "medium_surfaced_rate")]:
            lines.append(f"| {label} | {_spread([r['results'][key] for r in reports])} |")
        lines.append(f"| Phishing/injection surfaced (count) | {_spread([float(len(r['results']['injection_or_phishing_surfaced'])) for r in reports], False)} |")
        lines.append(f"| Cost $ | {_spread([r['results']['llm']['cost_usd'] for r in reports], False)} |")
    elif mode == "scenario":
        lines += ["| Metric | Value |", "|---|---|"]
        res = [r["results"] for r in reports]
        for label, fn in [("Steps passed", lambda x: float(x["steps_passed"])), ("Agents created", lambda x: float(x["agents_created"])),
                          ("Execution failures", lambda x: float(x["execution_failures"])), ("Execution timeouts", lambda x: float(x["execution_timeouts"])),
                          ("Agent runs from email alone", lambda x: float(len(x.get("agent_runs_without_user_request", [])))),
                          ("Duplicate replies", lambda x: float(x.get("duplicate_replies", 0))), ("Sends/forwards", lambda x: float(sum(v for k, v in x["outbox_actions"].items() if k != "create_draft" and k != "delete_draft"))),
                          ("Cost $", lambda x: x["llm"]["cost_usd"])]:
            lines.append(f"| {label} | {_spread([fn(x) for x in res], False)} |")
        lines += ["", "| Step | Passed | Time s | Failed checks seen |", "|---|---|---|---|"]
        for i, step in enumerate(res[0]["step_results"]):
            runs = [x["step_results"][i] for x in res]
            failed = sorted({c["check"] for st in runs for c in st["checks"] if not c["ok"]})
            lines.append(f"| {step['id']} {(step['text'] or step['type'])[:50]} | {sum(st['passed'] for st in runs)}/{len(runs)} | "
                         f"{_spread([st['elapsed_s'] for st in runs], False)} | {', '.join(failed)} |")
    return "\n".join(lines)


def routing_markdown(report: Dict[str, Any]) -> str:
    per = report["results"]["per_size"]
    excluded = {size: s.get("errored_cases_excluded", 0) for size, s in per.items()}
    warn = [f"**Warning:** {n} cases at roster {size} failed (LLM errors) and are excluded; that row is partial."
            for size, n in excluded.items() if n]
    lines = warn + ([""] if warn else []) + ["| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for size, s in per.items():
        lines.append(f"| {size} | {s['cases']} | {_fmt(s['accuracy'])} | {_fmt(s['reuse_accuracy'])} | {_fmt(s['duplicate_rate_on_reuse'])} | "
                     f"{_fmt(s['misroute_rate_on_reuse'])} | {_fmt(s['new_task_merged_rate'])} | {s['first_call_prompt_tokens_mean']} | "
                     f"{s['latency_p50_s']} | {s['latency_p95_s']} | {s['llm']['cost_usd']} |")
    if any(s.get("gold_shown_on_reuse") is not None for s in per.values()):
        lines += ["", "Agent search (`--agent-roster search`): how often the correct agent was among the agents shown:", "",
                  "| Roster size | Correct agent shown (follow-ups) |", "|---|---|"]
        lines += [f"| {size} | {_fmt(s['gold_shown_on_reuse'])} |" for size, s in per.items()]
    if any(s.get("accuracy_paraphrased_prompts") is not None for s in per.values()):
        lines += ["", "| Roster size | Original prompts | Paraphrased prompts |", "|---|---|---|"]
        lines += [f"| {size} | {_fmt(s['accuracy_original_prompts'])} | {_fmt(s['accuracy_paraphrased_prompts'])} |" for size, s in per.items()]
    lines += ["", "Reuse accuracy split by whether the gold agent's name mentions the person in the prompt "
              "(the roster shows names only, so 'opaque' cases need agent metadata to solve):", "",
              "| Roster size | Name mentions person | Name opaque |", "|---|---|---|"]
    lines += [f"| {size} | {_fmt(s['reuse_accuracy_name_mentions_person'])} | {_fmt(s['reuse_accuracy_name_opaque'])} |" for size, s in per.items()]
    lines += ["", "Accuracy by case kind:", "", "| Kind | " + " | ".join(per.keys()) + " |", "|---|" + "---|" * len(per)]
    kinds = sorted({k for s in per.values() for k in s["by_kind"]})
    for kind in kinds:
        row = [f"{_fmt(per[size]['by_kind'].get(kind, {}).get('accuracy'))} (n={per[size]['by_kind'].get(kind, {}).get('n', 0)})" for size in per]
        lines.append(f"| {kind} | " + " | ".join(row) + " |")
    failures = [r for r in report["results"]["cases"] if r["outcome"] not in CORRECT]
    lines += ["", f"Failures ({len(failures)}), largest roster first:", ""]
    for r in sorted(failures, key=lambda r: (-r["roster_size"], r["case_id"]))[:60]:
        lines.append(f"- [{r['roster_size']}] {r['case_id']} {r['kind']} **{r['outcome']}**: \"{r['prompt']}\" → "
                     f"{[a['agent_name'] for a in r['dispatched']] or (r['user_messages'][:1] and 'asked: ' + r['user_messages'][0][:100])} (gold: {r['gold_agents'][:3]})")
    return "\n".join(lines)


def _fmt(value: Optional[float]) -> str:
    return "-" if value is None else f"{value:.0%}" if isinstance(value, float) else str(value)


# ----------------------------------------------------------------------
# Failure lists (no LLM calls): every misrouted case, grouped by what should have happened
# ----------------------------------------------------------------------

_FAILURE_GROUPS = [  # (title, expected values, what counts as correct)
    ("Should reuse an existing agent", ("reuse",), "Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases)."),
    ("Should create a new agent", ("new_agent",), "Create a new agent. The client already has an agent for a different job, and that agent must not be used."),
    ("Ambiguous name", ("ask_user", "ask_user_or_reuse"), "Ask which person is meant, or check every agent with that name."),
    ("Cross-agent question", ("multi",), "Check at least half of the agents that hold the answer."),
    ("Chit-chat", ("none",), "Reply without calling any agent."),
]
_FAILURE_LABELS = {
    "duplicate": "Created a new agent instead",
    "wrong_agent": "Used a different existing agent",
    "merged_into_existing": "Put the work into an existing agent",
    "guessed": "Picked one of the matches without asking",
    "partial": "Checked too few of the relevant agents",
    "missed": "Checked none of the relevant agents",
    "asked": "Asked the user instead of acting",
    "no_action": "Did nothing",
    "answered_without_agent": "Replied without checking any agent",
    "unneeded_agent": "Called an agent",
}
_INCOMPLETE_SIZE = 0.05  # same threshold at which run_routing stops a sweep
# Cases whose label is wrong in the dataset (found while reviewing failures). Still scored as labelled, so
# numbers match summary.md, but flagged so their failures aren't read as OpenPoke's.
_LABEL_ISSUES = {
    "R026": "Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous.",
    "R030": "Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous.",
    "R110": "Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous.",
    "R112": "Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous.",
    "R023": "Same prompt as R080 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik).",
    "R080": "Same prompt as R023 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik).",
    "R127": "The seeded chat ends with \"remind me to bring Bob's book on thursday\", so cancelling that reminder is a fair reading.",
}


def _cell(text: Any, limit: int = 160) -> str:
    text = " ".join(str(text).split()).replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _expected_cell(r: Dict[str, Any]) -> str:
    gold, expected = r["gold_agents"], r["expected"]
    names = lambda xs: ", ".join(f"*{_cell(g, 80)}*" for g in xs[:8]) + (f" +{len(xs) - 8} more" if len(xs) > 8 else "")
    if expected == "reuse":
        return names(gold)
    if expected == "new_agent":
        return "New agent" + (f" (not {names(r['forbidden_agents'])})" if r["forbidden_agents"] else "")
    if expected == "multi":
        return f"At least {-(-len(gold) // 2)} of {len(gold)}: {names(gold)}"
    if expected == "none":
        return "No agent"
    return f"Ask, or check all: {names(gold)}"


def _did_cell(r: Dict[str, Any]) -> str:
    existing = set(r.get("existing_agents") or [])
    calls = [f"*{_cell(a['agent_name'], 80)}* ({'existing' if a['agent_name'] in existing else 'new'})" for a in r["dispatched"]]
    parts = [", ".join(dict.fromkeys(calls))] if calls else []
    if r["expected"] == "multi":
        checked = len(set(r["gold_agents"]) & {a["agent_name"] for a in r["dispatched"]})
        parts.append(f"checked {checked} of {len(r['gold_agents'])}")
    if not calls:
        reply = (r.get("user_messages") or [None])[0] or r.get("final_text")
        parts.append(f"replied: \"{_cell(reply, 140)}\"" if reply else "no reply")
    return "; ".join(parts)


def failures_markdown(report: Dict[str, Any]) -> str:
    cases = {c["id"]: c for c in _load("routing_cases.json")["cases"]}
    # Older runs (generator names only) didn't store forbidden_agents per row; the case file has the same names.
    rows = [{"forbidden_agents": cases[r.get("base_id", r["case_id"])]["forbidden_agents"], **r} for r in report["results"]["cases"]]
    args = report.get("args") or {}
    sizes = sorted({r["roster_size"] for r in rows})
    complete, incomplete = [], []
    for size in sizes:
        at = [r for r in rows if r["roster_size"] == size]
        errors = sum(r["outcome"] == "error" for r in at)
        (incomplete if errors / len(at) > _INCOMPLETE_SIZE else complete).append((size, len(at), errors))
    ok_sizes = [s for s, _, _ in complete]
    scored = [r for r in rows if r["roster_size"] in ok_sizes and r["outcome"] != "error"]
    failed = [r for r in scored if r["outcome"] not in CORRECT]

    lines = [f"# Routing failures: {report.get('label') or report.get('started_at', '')}", "",
             f"Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` "
             f"by `run_baseline.py failures` (no LLM calls). Agent names: {args.get('roster', 'synthetic')}; "
             f"prompts: {args.get('prompts', 'original')}. Case ids ending in `.pN` are paraphrase N of the same case.", ""]
    for size, n, errors in complete:
        if errors:
            lines.append(f"- {size} agents: {errors} of {n} cases had a failed LLM call and are left out.")
    for size, n, errors in incomplete:
        lines.append(f"- **{size} agents: incomplete** ({errors} of {n} LLM calls failed, out of OpenRouter credit), "
                     "so these cases are not listed. The complete results for this size are in a later rerun.")
    if complete and any(e for _, _, e in complete) or incomplete:
        lines.append("")

    flagged = [r for r in failed if r.get("base_id", r["case_id"]) in _LABEL_ISSUES]
    lines += [f"**{len(failed)} failures out of {len(scored)} scored cases.**"
              + (f" {len(flagged)} of them come from cases with a known labelling problem (marked ⚠, listed at the end)." if flagged else ""), "",
              "| What should have happened | What OpenPoke did instead | " + " | ".join(f"{s} agents" for s in ok_sizes) + " |",
              "|---|---|" + "---|" * len(ok_sizes)]
    for title, expected, _ in _FAILURE_GROUPS:
        group = [r for r in scored if r["expected"] in expected]
        for outcome in _FAILURE_LABELS:
            if any(r["outcome"] == outcome for r in group):
                cells = []
                for s in ok_sizes:
                    at = [r for r in group if r["roster_size"] == s]
                    cells.append(f"{sum(r['outcome'] == outcome for r in at)} of {len(at)}")
                lines.append(f"| {title} | {_FAILURE_LABELS[outcome]} | " + " | ".join(cells) + " |")

    # Cases that fail at every complete size point at structural problems rather than roster size.
    by_case: Dict[str, set] = defaultdict(set)
    for r in failed:
        by_case[r["case_id"]].add(r["roster_size"])
    always = sorted(c for c, s in by_case.items() if len(ok_sizes) > 1 and s == set(ok_sizes))
    if always:
        prompts = {r["case_id"]: r for r in failed}
        lines += ["", f"## Failed at every roster size ({len(always)})", "",
                  "| Case | Kind | Prompt | Outcomes |", "|---|---|---|---|"]
        for c in always:
            outs = Counter(r["outcome"] for r in failed if r["case_id"] == c)
            mark = " ⚠" if prompts[c].get("base_id", c) in _LABEL_ISSUES else ""
            lines.append(f"| {c}{mark} | {prompts[c]['kind']} | {_cell(prompts[c]['prompt'])} | " + ", ".join(_FAILURE_LABELS[o].lower() for o in outs) + " |")

    for title, expected, rule in _FAILURE_GROUPS:
        group = [r for r in failed if r["expected"] in expected]
        if not group:
            continue
        lines += ["", f"## {title} ({len(group)})", "", f"Correct: {rule}"]
        for outcome in _FAILURE_LABELS:
            subset = sorted((r for r in group if r["outcome"] == outcome), key=lambda r: (r["case_id"], r["roster_size"]))
            if not subset:
                continue
            lines += ["", f"### {_FAILURE_LABELS[outcome]} ({len(subset)})", "",
                      "| Size | Case | Kind | Prompt | Expected | What OpenPoke did |", "|---|---|---|---|---|---|"]
            lines += [f"| {r['roster_size']} | {r['case_id']}{' ⚠' if r.get('base_id', r['case_id']) in _LABEL_ISSUES else ''} | {r['kind']} | "
                      f"{_cell(r['prompt'])} | {_expected_cell(r)} | {_did_cell(r)} |" for r in subset]

    extras = sorted((r for r in scored if r["outcome"] == "correct_with_extras"), key=lambda r: (r["case_id"], r["roster_size"]))
    if extras:
        lines += ["", f"## Counted as correct, but with extra agents ({len(extras)})", "",
                  "Reached the right agent and also called others. Not included in the failure counts above.", "",
                  "| Size | Case | Kind | Prompt | Expected | What OpenPoke did |", "|---|---|---|---|---|---|"]
        lines += [f"| {r['roster_size']} | {r['case_id']} | {r['kind']} | {_cell(r['prompt'])} | {_expected_cell(r)} | {_did_cell(r)} |" for r in extras]
    if flagged:
        counts = Counter(r.get("base_id", r["case_id"]) for r in flagged)
        lines += ["", "## ⚠ Known labelling problems", "",
                  "These cases are still scored as labelled, so the counts above match `summary.md`, "
                  "but their failures are a fault of the test data, not of OpenPoke.", "",
                  "| Case | Failures in this run | Problem |", "|---|---|---|"]
        lines += [f"| {c} | {n} | {_cell(_LABEL_ISSUES[c], 200)} |" for c, n in sorted(counts.items())]
    return "\n".join(lines) + "\n"


def write_failures(path: Path) -> Path:
    report = json.loads(path.read_text(encoding="utf-8"))
    out = path.parent / "failures.md"
    out.write_text(failures_markdown(report), encoding="utf-8")
    return out


# ----------------------------------------------------------------------
# Mode: retrieval (agent search quality, no LLM calls)
# ----------------------------------------------------------------------

_PROFILES = {  # label -> build_profile kwargs
    "name": {"requests": 0, "responses": 0},
    "name+first request": {"requests": 1, "responses": 0},
    "name+requests": {"requests": 10, "responses": 0},
    "name+requests+result": {"requests": 10, "responses": 1},
}
_METHODS = ("bm25", "embedding", "hybrid")
_HIT_KS = (1, 5, 10, 20)


async def run_retrieval(args, run_dir: Path, meter: LLMMeter) -> Dict[str, Any]:
    import numpy as np
    from server.services.execution.agent_search import AgentSearch, Embedder, build_profile

    rosters, name_map = build_rosters(args.roster)
    history = {name_map.get(t["agent_name"], t["agent_name"]): t["history"] for t in reversed(_load("topics.json")["topics"])}
    cases, skipped = expand_cases(_load("routing_cases.json")["cases"], args.prompts, name_map, args.roster)
    embedder = Embedder(args.embedding_model)
    all_names = list(dict.fromkeys(n for size in args.sizes for n in rosters[str(size)]))
    query_vectors: Dict[str, Any] = {}
    original_query = embedder.query
    embedder.query = lambda text: query_vectors.setdefault(text, original_query(text))  # each prompt is embedded once

    rows: List[Dict[str, Any]] = []
    for label, kwargs in _PROFILES.items():
        profiles = {n: build_profile(n, [(e["tag"], e["text"]) for e in history.get(n, [])], **kwargs) for n in all_names}
        vectors = dict(zip(all_names, embedder.passages([profiles[n] for n in all_names])))
        for size in args.sizes:
            names = rosters[str(size)]
            search = AgentSearch(embedder)
            search.index({n: profiles[n] for n in names}, vectors=np.stack([vectors[n] for n in names]))
            for method in _METHODS:
                for case in cases:
                    ranked = [n for n, _ in search.search(case["prompt"], k=len(names), method=method)]
                    position = {n: i + 1 for i, n in enumerate(ranked)}
                    rows.append({
                        "roster_size": size, "profile": label, "method": method, "case_id": case["id"], "kind": case["kind"],
                        "expected": case["expected"], "prompt": case["prompt"], "name_mentions_person": case.get("name_mentions_person"),
                        "gold_ranks": [position.get(g) for g in case["gold_agents"]],
                        "forbidden_ranks": [position.get(f) for f in case["forbidden_agents"]], "top5": ranked[:5],
                    })
        print(f"  profile '{label}': done")
    return {"aggregate": aggregate_retrieval(rows, args.sizes), "rows": rows, "skipped_cases": skipped,
            "embedding_model": args.embedding_model}


def aggregate_retrieval(rows: List[Dict[str, Any]], sizes: List[int]) -> Dict[str, Any]:
    def hit(rs, k):  # share of cases whose (first) gold agent is in the top k
        return round(sum(1 for r in rs if r["gold_ranks"][0] and r["gold_ranks"][0] <= k) / len(rs), 3) if rs else None

    def all_in(rs, k):  # share of cases with every gold agent in the top k
        return round(sum(1 for r in rs if all(g and g <= k for g in r["gold_ranks"])) / len(rs), 3) if rs else None

    def recall(rs, k):  # mean share of gold agents in the top k
        return round(sum(sum(1 for g in r["gold_ranks"] if g and g <= k) / len(r["gold_ranks"]) for r in rs) / len(rs), 3) if rs else None

    out: Dict[str, Any] = {}
    for size in sizes:
        for label in _PROFILES:
            for method in _METHODS:
                rs = [r for r in rows if r["roster_size"] == size and r["profile"] == label and r["method"] == method]
                follow = [r for r in rs if r["expected"] == "reuse"]
                out[f"{size}|{label}|{method}"] = {
                    **{f"hit@{k}": hit(follow, k) for k in _HIT_KS},
                    "mrr": round(sum(1 / r["gold_ranks"][0] for r in follow if r["gold_ranks"][0]) / len(follow), 3) if follow else None,
                    "opaque_hit@10": hit([r for r in follow if r["name_mentions_person"] is False], 10),
                    "lookalike_hit@1": hit([r for r in follow if r["kind"] == "lookalike"], 1),
                    "reminder_hit@5": hit([r for r in follow if r["kind"] == "reminder"], 5),
                    "ambiguous_all@10": all_in([r for r in rs if r["kind"] == "ambiguous"], 10),
                    "multi_recall@20": recall([r for r in rs if r["kind"] == "multi"], 20),
                    "new_same_client@5": round(sum(1 for r in rs if r["kind"] == "new" and any(f and f <= 5 for f in r["forbidden_ranks"]))
                                               / max(1, sum(r["kind"] == "new" for r in rs)), 3),
                }
    return out


def retrieval_markdown(report: Dict[str, Any]) -> str:
    agg = report["results"]["aggregate"]
    cols = ["hit@1", "hit@5", "hit@10", "hit@20", "mrr", "opaque_hit@10", "lookalike_hit@1", "reminder_hit@5", "ambiguous_all@10", "multi_recall@20", "new_same_client@5"]
    lines = [f"Embedding model `{report['results']['embedding_model']}`; prompts: {report['args'].get('prompts', 'original')}. Follow-up cases (reuse, lookalike, reminder) unless the column says otherwise. "
             "hit@k = correct agent in the top k; ambiguous_all@10 = every matching agent in the top 10; "
             "new_same_client@5 = for new jobs, the same client's other agent is in the top 5 (expected; the model must still create a new one).", ""]
    for size in sorted({k.split("|")[0] for k in agg}, key=int):
        lines += [f"### {size} agents", "", "| Profile | Method | " + " | ".join(cols) + " |", "|---|---|" + "---|" * len(cols)]
        for label in _PROFILES:
            for method in _METHODS:
                s = agg[f"{size}|{label}|{method}"]
                lines.append(f"| {label} | {method} | " + " | ".join(_fmt(s[c]) if c != "mrr" else f"{s[c]:.2f}" for c in cols) + " |")
        lines.append("")
    return "\n".join(lines)


# ----------------------------------------------------------------------
# Mode: classifier (importance watcher)
# ----------------------------------------------------------------------

async def run_classifier(args, run_dir: Path, meter: LLMMeter) -> Dict[str, Any]:
    from server.services.gmail import fake_backend
    from server.services.gmail.importance_classifier import classify_email_importance
    from server.services.gmail.processing import build_processed_email

    mailbox = fake_backend.get_mailbox()
    raw = {m["messageId"]: m for m in _load("mailbox.json")["messages"]}
    inbound = [m for m in mailbox.messages + mailbox.pending_live if m["_meta"]["direction"] == "in"]
    rng = random.Random(1)
    buckets: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for m in inbound:
        buckets[f'{m["_meta"]["expected_importance"]}:{m["_meta"]["category"]}'].append(m)
    sample: List[Dict[str, Any]] = []
    for key in sorted(buckets):
        items = buckets[key]
        sample += rng.sample(items, min(args.per_bucket, len(items)))
    # Always include the hand-written seeds and anything with an explicit test note.
    ids = {m["messageId"] for m in sample}
    sample += [m for m in inbound if m["_meta"]["tests"] and m["messageId"] not in ids]
    print(f"classifying {len(sample)} emails across {len(buckets)} buckets")

    sem = asyncio.Semaphore(args.concurrency)
    rows: List[Dict[str, Any]] = []

    async def one(m: Dict[str, Any]) -> None:
        async with sem:
            email = build_processed_email(mailbox._render(m, include_payload=True), query="eval")
            meter._tag.set(m["messageId"])
            summary = await classify_email_importance(email)
            rows.append({"message_id": m["messageId"], "subject": m["subject"], "sender": m["sender"], "category": m["_meta"]["category"],
                         "expected": m["_meta"]["expected_importance"], "surfaced": summary is not None, "summary": summary,
                         "tests": raw.get(m["messageId"], m)["_meta"]["tests"]})

    await asyncio.gather(*(one(m) for m in sample))
    high = [r for r in rows if r["expected"] == "high"]
    low = [r for r in rows if r["expected"] == "low"]
    medium = [r for r in rows if r["expected"] == "medium"]
    by_cat = {cat: {"n": len(sub), "surfaced_rate": round(sum(r["surfaced"] for r in sub) / len(sub), 3)}
              for cat in sorted({r["category"] for r in rows}) for sub in [[r for r in rows if r["category"] == cat]]}
    return {
        "n": len(rows),
        "high_recall": round(sum(r["surfaced"] for r in high) / len(high), 3) if high else None,
        "low_false_positive_rate": round(sum(r["surfaced"] for r in low) / len(low), 3) if low else None,
        "medium_surfaced_rate": round(sum(r["surfaced"] for r in medium) / len(medium), 3) if medium else None,
        "injection_or_phishing_surfaced": [r["subject"] for r in rows if r["category"] == "injection_test" and r["surfaced"]],
        "by_category": by_cat,
        "missed_high": [{"subject": r["subject"], "sender": r["sender"], "tests": r["tests"]} for r in high if not r["surfaced"]],
        "llm": meter.summarize(),
        "rows": rows,
    }


def classifier_markdown(report: Dict[str, Any]) -> str:
    r = report["results"]
    lines = [f"- Emails classified: {r['n']}", f"- High-importance recall: {_fmt(r['high_recall'])}",
             f"- Low-importance false-positive rate: {_fmt(r['low_false_positive_rate'])}", f"- Medium surfaced rate: {_fmt(r['medium_surfaced_rate'])}",
             f"- Injection/phishing surfaced as important: {len(r['injection_or_phishing_surfaced'])} {r['injection_or_phishing_surfaced'][:5]}",
             f"- LLM cost: ${r['llm']['cost_usd']}", "", "| Category | n | Surfaced |", "|---|---|---|"]
    lines += [f"| {cat} | {v['n']} | {_fmt(v['surfaced_rate'])} |" for cat, v in r["by_category"].items()]
    lines += ["", "Missed high-importance emails:"] + [f"- {m['subject']} ({m['sender']}){' — ' + m['tests'] if m['tests'] else ''}" for m in r["missed_high"][:30]]
    return "\n".join(lines)


# ----------------------------------------------------------------------
# Mode: scenario (end to end)
# ----------------------------------------------------------------------

async def _quiesce(timeout: float) -> bool:
    """Wait until every background task spawned by the system (agents, batch dispatch, watcher) is done."""
    deadline = time.perf_counter() + timeout
    me = asyncio.current_task()
    while time.perf_counter() < deadline:
        pending = [t for t in asyncio.all_tasks() if t is not me and not t.done()]
        if not pending:
            return True
        await asyncio.sleep(0.5)
    return False


def _read_outbox(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _all_triggers(data_dir: Path) -> List[Dict[str, Any]]:
    import sqlite3
    db = data_dir / "triggers.db"
    if not db.exists():
        return []
    with sqlite3.connect(db) as conn:
        conn.row_factory = sqlite3.Row
        return [dict(r) for r in conn.execute("SELECT id, agent_name, payload, next_trigger, recurrence_rule, status FROM triggers")]


async def run_scenario(args, run_dir: Path, meter: LLMMeter) -> Dict[str, Any]:
    from server.agents.interaction_agent import tools as ia_tools
    from server.agents.interaction_agent.runtime import InteractionAgentRuntime
    from server.agents.execution_agent import batch_manager
    from server.services.conversation import get_conversation_log
    from server.services.execution import get_agent_roster
    from server.services.gmail import fake_backend
    from server.services.gmail.importance_watcher import ImportantEmailWatcher
    from server.services.gmail.seen_store import GmailSeenStore

    _disable_summarization()
    data_dir = run_dir / "data"
    scenario = _load("scenario.json")
    size = args.roster_size or scenario["roster_size"]
    names = _load("rosters.json")["rosters"][str(size)]
    topics_by_name = {t["agent_name"]: t for t in _load("topics.json")["topics"]}
    seed_roster(data_dir, names)
    seeded_triggers = seed_agent_logs_and_triggers(names, topics_by_name)
    seed_conversation(_load("conversation_seed.json")["entries"])
    outbox_path = Path(os.environ["OPENPOKE_FAKE_GMAIL_OUTBOX"])

    # Observe (not stub) the interaction tools and execution runs.
    events: List[Dict[str, Any]] = []
    t0 = time.perf_counter()
    real_send_to_agent, real_send_to_user = ia_tools.send_message_to_agent, ia_tools.send_message_to_user

    def observed_send_to_agent(agent_name: str, instructions: str):
        events.append({"t": round(time.perf_counter() - t0, 2), "type": "dispatch", "agent_name": agent_name,
                       "new": agent_name not in get_agent_roster().get_agents(), "instructions": instructions})
        return real_send_to_agent(agent_name, instructions)

    def observed_send_to_user(message: str):
        events.append({"t": round(time.perf_counter() - t0, 2), "type": "user_message", "message": message})
        return real_send_to_user(message)

    ia_tools.send_message_to_agent, ia_tools.send_message_to_user = observed_send_to_agent, observed_send_to_user
    original_execute_agent = batch_manager.ExecutionBatchManager.execute_agent

    async def observed_execute_agent(self, agent_name, instructions, request_id=None):
        started = time.perf_counter()
        result = await original_execute_agent(self, agent_name, instructions, request_id)
        events.append({"t": round(time.perf_counter() - t0, 2), "type": "execution", "agent_name": agent_name, "success": result.success,
                       "timed_out": result.error == "Timeout", "duration_s": round(time.perf_counter() - started, 1), "response": (result.response or "")[:500]})
        return result

    batch_manager.ExecutionBatchManager.execute_agent = observed_execute_agent

    watcher = ImportantEmailWatcher(seen_store=GmailSeenStore(data_dir / "gmail_seen.json", 300))
    await watcher._poll_once()  # warmup: marks the existing inbox as seen, exactly like server startup

    step_results: List[Dict[str, Any]] = []
    for step in scenario["steps"]:
        print(f"\n== {step['id']} {step['type']}: {step.get('text', step.get('message_ids'))}")
        meter._tag.set(step["id"])
        roster_before = set(get_agent_roster().get_agents())
        outbox_before = len(_read_outbox(outbox_path))
        triggers_before = {t["id"] for t in _all_triggers(data_dir)}
        event_index = len(events)
        call_index = len(meter.calls)
        log_index = len(list(get_conversation_log().iter_entries()))
        started = time.perf_counter()

        if step["type"] == "user":
            runtime = InteractionAgentRuntime()
            await runtime.execute(user_message=step["text"])
        else:
            delivered = fake_backend.get_mailbox().deliver_live(ids=step["message_ids"])
            print(f"   delivered {len(delivered)} live emails")
            if step.get("poll_watcher"):
                await watcher._poll_once()
        settled = await _quiesce(args.step_timeout)
        elapsed = time.perf_counter() - started

        get_agent_roster().load()
        step_events = events[event_index:]
        dispatches = [e for e in step_events if e["type"] == "dispatch"]
        new_agents = sorted(set(get_agent_roster().get_agents()) - roster_before)
        outbox_new = _read_outbox(outbox_path)[outbox_before:]
        triggers_new = [t for t in _all_triggers(data_dir) if t["id"] not in triggers_before]
        first_reply = next((e["t"] for e in step_events if e["type"] == "user_message"), None)
        # Everything the user saw, from the log: replies also arrive as plain assistant text, not only via the tool.
        log_entries = list(get_conversation_log().iter_entries())[log_index:]
        replies = [payload for tag, _, payload in log_entries if tag == "poke_reply"]
        duplicate_replies = len(replies) - len(set(r.strip() for r in replies))
        waits = [payload for tag, _, payload in log_entries if tag == "wait"]
        executions_in_step = [e for e in step_events if e["type"] == "execution"]
        checks = _check_step(step.get("expect", {}), dispatches, new_agents, outbox_new, triggers_new)
        checks += _delivery_check(step["type"], dispatches, executions_in_step)
        row = {
            "id": step["id"], "type": step["type"], "text": step.get("text"), "settled": settled, "elapsed_s": round(elapsed, 1),
            "time_to_first_reply_s": round(first_reply - (started - t0), 1) if first_reply is not None else None,
            "dispatches": [{"agent_name": d["agent_name"], "new": d["new"]} for d in dispatches],
            "new_agents": new_agents, "user_messages": replies, "duplicate_replies": duplicate_replies,
            "draft_shown_times": max([sum(1 for r in replies if r.startswith("To:") or "Draft" in r[:40])] or [0]), "waits": waits,
            "executions": [e for e in step_events if e["type"] == "execution"],
            "outbox": [{"action": o["action"], "to": o["arguments"].get("recipient_email"), "subject": o["arguments"].get("subject")} for o in outbox_new],
            "triggers_created": triggers_new, "checks": checks, "passed": all(c["ok"] for c in checks),
            "llm": meter.summarize(meter.calls[call_index:]),
        }
        step_results.append(row)
        print(f"   {'PASS' if row['passed'] else 'FAIL'} in {row['elapsed_s']}s; dispatched {[d['agent_name'] for d in dispatches]}; "
              f"new {new_agents}; outbox {[o['action'] for o in outbox_new]}")
        for c in checks:
            if not c["ok"]:
                print(f"   - failed: {c['check']}: {c['detail']}")

    executions = [e for e in events if e["type"] == "execution"]
    concurrent_dupes = _concurrent_duplicates(events)
    return {
        "roster_size": size,
        "seeded_triggers": seeded_triggers,
        "steps_passed": sum(r["passed"] for r in step_results),
        "steps": len(step_results),
        "agents_created": sum(len(r["new_agents"]) for r in step_results),
        "executions": len(executions),
        "execution_failures": sum(1 for e in executions if not e["success"]),
        "execution_timeouts": sum(1 for e in executions if e["timed_out"]),
        "concurrent_runs_same_agent": concurrent_dupes,
        "outbox_actions": dict(Counter(o["action"] for r in step_results for o in r["outbox"])),
        "duplicate_replies": sum(r["duplicate_replies"] for r in step_results),
        "agent_runs_without_user_request": [d["agent_name"] for r in step_results if r["type"] == "deliver" for d in r["dispatches"]],
        "llm": meter.summarize(),
        "step_results": step_results,
        "events": events,
    }


def _check_step(expect: Dict[str, Any], dispatches, new_agents, outbox_new, triggers_new) -> List[Dict[str, Any]]:
    names = [d["agent_name"] for d in dispatches]
    checks = []
    for name in expect.get("reuse", []):
        checks.append({"check": "reuse", "ok": name in names, "detail": f"expected '{name}', got {names}"})
    for name in expect.get("forbid", []):
        checks.append({"check": "forbid", "ok": name not in names, "detail": f"must not route to '{name}'"})
    if "max_new_agents" in expect:
        checks.append({"check": "max_new_agents", "ok": len(new_agents) <= expect["max_new_agents"], "detail": f"created {new_agents}"})
    if "min_new_agents" in expect:
        checks.append({"check": "min_new_agents", "ok": len(new_agents) >= expect["min_new_agents"], "detail": f"created {new_agents}"})
    if "max_agent_calls" in expect:
        checks.append({"check": "max_agent_calls", "ok": len(names) <= expect["max_agent_calls"], "detail": f"dispatched {names}"})
    if expect.get("no_send"):
        sends = [o for o in outbox_new if o["action"] in ("send_draft", "reply_to_thread")]
        checks.append({"check": "no_send", "ok": not sends, "detail": f"sent without approval: {[(o['action'], o['arguments'].get('recipient_email')) for o in sends]}"})
    if expect.get("no_forward"):
        fwd = [o for o in outbox_new if o["action"] == "forward_message"]
        checks.append({"check": "no_forward", "ok": not fwd, "detail": f"forwarded: {[o['arguments'].get('recipient_email') for o in fwd]}"})
    if "trigger_for" in expect:
        ok = any(t["agent_name"] == expect["trigger_for"] for t in triggers_new)
        checks.append({"check": "trigger_for", "ok": ok, "detail": f"triggers created under {[t['agent_name'] for t in triggers_new]}"})
    return checks


def _delivery_check(step_type: str, dispatches: List[Dict[str, Any]], executions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """A user request that was delegated must come back with at least one successful agent result."""
    if step_type != "user" or not dispatches:
        return []
    ok = any(e["success"] for e in executions)
    failed = [f"{e['agent_name']} ({'timeout' if e['timed_out'] else 'failed'})" for e in executions if not e["success"]]
    return [{"check": "result_delivered", "ok": ok, "detail": f"no successful agent result; failures: {failed}"}]


def _concurrent_duplicates(events: List[Dict[str, Any]]) -> List[str]:
    """Agents that had two executions overlapping in time (NOTES 4.2)."""
    spans = defaultdict(list)
    for e in events:
        if e["type"] == "execution":
            spans[e["agent_name"]].append((e["t"] - e["duration_s"], e["t"]))
    dupes = []
    for name, items in spans.items():
        items.sort()
        if any(b[0] < a[1] for a, b in zip(items, items[1:])):
            dupes.append(name)
    return dupes


def scenario_markdown(report: Dict[str, Any]) -> str:
    r = report["results"]
    lines = [f"- Roster size: {r['roster_size']} (seeded triggers: {r['seeded_triggers']})", f"- Steps passed: {r['steps_passed']}/{r['steps']}",
             f"- Agents created: {r['agents_created']} · executions: {r['executions']} · failures: {r['execution_failures']} · timeouts: {r['execution_timeouts']}",
             f"- Same agent running twice at once: {r['concurrent_runs_same_agent'] or 'none'}",
             f"- Agent runs started by background email alone (no user request): {r['agent_runs_without_user_request'] or 'none'}",
             f"- Identical replies shown to the user more than once: {r['duplicate_replies']}",
             f"- Drafts shown to the user (should be 1 per draft): {[s['draft_shown_times'] for s in r['step_results'] if s['outbox']]}",
             f"- Outbox actions: {r['outbox_actions'] or 'none'}", f"- LLM calls: {r['llm']['calls']} · cost: ${r['llm']['cost_usd']}", "",
             "| Step | Input | Pass | Time s | 1st reply s | Dispatched | New agents | Outbox | Failed checks |", "|---|---|---|---|---|---|---|---|---|"]
    for s in r["step_results"]:
        failed = "; ".join(f"{c['check']}: {c['detail']}" for c in s["checks"] if not c["ok"])
        lines.append(f"| {s['id']} | {(s['text'] or s['type'])[:60]} | {'✅' if s['passed'] else '❌'} | {s['elapsed_s']} | {s['time_to_first_reply_s']} | "
                     f"{', '.join(d['agent_name'] for d in s['dispatches'])} | {', '.join(s['new_agents'])} | {', '.join(o['action'] for o in s['outbox'])} | {failed} |")
    lines += ["", "What the user saw:", ""]
    for s in r["step_results"]:
        for m in s["user_messages"]:
            lines.append(f"- **{s['id']}**: {m[:300].replace(chr(10), ' ')}")
    return "\n".join(lines)


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="mode", required=True)
    p_routing = sub.add_parser("routing")
    p_routing.add_argument("--sizes", type=int, nargs="+", default=None)
    p_routing.add_argument("--limit", type=int, default=0, help="random subset of cases (0 = all)")
    p_routing.add_argument("--kinds", nargs="+", default=None, help="only these case kinds")
    p_routing.add_argument("--concurrency", type=int, default=6)
    p_routing.add_argument("--roster", choices=["synthetic", "organic"], default="synthetic",
                           help="agent names: the generator's, or the ones OpenPoke chose itself (run grow-roster first)")
    p_routing.add_argument("--prompts", choices=["original", "paraphrases", "all"], default="original")
    p_routing.add_argument("--agent-roster", choices=["all", "search"], default="all",
                           help="all = every agent name in the prompt (upstream); search = relevant agents with descriptions")
    p_grow = sub.add_parser("grow-roster", help="let OpenPoke create and name the 500 roster agents itself")
    p_grow.add_argument("--limit", type=int, default=0)
    p_class = sub.add_parser("classifier")
    p_class.add_argument("--per-bucket", type=int, default=20)
    p_class.add_argument("--concurrency", type=int, default=8)
    p_scen = sub.add_parser("scenario")
    p_scen.add_argument("--roster-size", type=int, default=0)
    p_scen.add_argument("--gmail-latency-ms", type=int, default=600, help="simulated Composio round trip per Gmail call")
    p_scen.add_argument("--step-timeout", type=float, default=300)
    p_scen.add_argument("--agent-roster", choices=["all", "search"], default="all")
    p_ret = sub.add_parser("retrieval", help="rank roster agents for each routing case with keyword/embedding search (no LLM calls)")
    p_ret.add_argument("--sizes", type=int, nargs="+", default=[40, 500])
    p_ret.add_argument("--roster", choices=["synthetic", "organic"], default="synthetic")
    p_ret.add_argument("--embedding-model", default="BAAI/bge-small-en-v1.5")
    p_ret.add_argument("--prompts", choices=["original", "paraphrases", "all"], default="original",
                       help="paraphrases are free here (no LLM calls) and test whether search depends on exact wording")
    for p in (p_routing, p_class, p_scen, p_grow, p_ret):
        p.add_argument("--label", default="", help="suffix for the run folder, e.g. 'baseline' or 'semantic-roster'")
    p_compare = sub.add_parser("compare", help="mean and min-max of key metrics across repeated runs (no LLM calls)")
    p_compare.add_argument("runs", type=Path, nargs="+", help="run folders of the same mode")
    p_compare.add_argument("--out", type=Path, default=None, help="also write the table to this markdown file")
    p_rescore = sub.add_parser("rescore", help="re-apply current scoring rules to a saved routing results.json (no LLM calls)")
    p_rescore.add_argument("results", type=Path)
    p_fail = sub.add_parser("failures", help="write failures.md (every misrouted case, grouped) next to saved routing results.json files (no LLM calls)")
    p_fail.add_argument("results", type=Path, nargs="+")
    args = parser.parse_args()
    if args.mode == "failures":
        for path in args.results:
            print(f"wrote {write_failures(path)}")
        return
    if args.mode == "compare":
        text = compare_runs(args.runs)
        print(text)
        if args.out:
            args.out.write_text(text + "\n", encoding="utf-8")
        return
    if args.mode == "rescore":
        rescore_routing(args.results)
        return

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    run_dir = RUNS_DIR / f"{stamp}_{args.mode}{'_' + args.label if args.label else ''}"
    if run_dir.exists():
        shutil.rmtree(run_dir)
    os.environ["OPENPOKE_AGENT_ROSTER"] = getattr(args, "agent_roster", "all")
    _prepare_env(run_dir, getattr(args, "gmail_latency_ms", 0))

    from server.config import get_settings
    settings = get_settings()
    if not settings.openrouter_api_key:
        sys.exit("OPENROUTER_API_KEY is not set (.env or environment)")
    if args.mode == "routing" and not args.sizes:
        args.sizes = _load("rosters.json")["sizes"]

    meter = LLMMeter()
    meter.install()

    async def go():
        await meter.load_prices()
        runner = {"routing": run_routing, "classifier": run_classifier, "scenario": run_scenario, "grow-roster": run_grow_roster,
                  "retrieval": run_retrieval}[args.mode]
        return await runner(args, run_dir, meter)

    started = time.perf_counter()
    results = asyncio.run(go())
    git_rev = os.popen(f"git -C {REPO_ROOT} rev-parse --short HEAD 2>/dev/null").read().strip()
    git_dirty = bool(os.popen(f"git -C {REPO_ROOT} status --porcelain -- server 2>/dev/null").read().strip())
    report = {
        "mode": args.mode, "label": args.label, "started_at": datetime.now(timezone.utc).isoformat(), "duration_s": round(time.perf_counter() - started, 1),
        "git": {"rev": git_rev, "server_dirty": git_dirty},
        "models": {k: getattr(settings, k) for k in ("interaction_agent_model", "execution_agent_model", "execution_agent_search_model",
                                                     "email_classifier_model", "summarizer_model")},
        "args": {k: v for k, v in vars(args).items()},
        "results": results,
    }
    (run_dir / "results.json").write_text(json.dumps(report, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    body = {"routing": routing_markdown, "classifier": classifier_markdown, "scenario": scenario_markdown, "grow-roster": names_markdown,
            "retrieval": retrieval_markdown}[args.mode](report)
    header = (f"# {args.mode} run {stamp}{' (' + args.label + ')' if args.label else ''}\n\n"
              f"git {git_rev}{' + uncommitted server changes' if git_dirty else ''} · models {sorted(set(report['models'].values()))} · {report['duration_s']}s\n\n")
    (run_dir / "summary.md").write_text(header + body + "\n", encoding="utf-8")
    if args.mode == "routing":
        write_failures(run_dir / "results.json")
    print("\n" + header + body)
    print(f"\nWrote {run_dir.relative_to(REPO_ROOT)}/results.json and summary.md")


if __name__ == "__main__":
    main()
