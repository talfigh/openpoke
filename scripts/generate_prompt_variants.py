#!/usr/bin/env python3
"""Generate LLM-written prompt variants for the synthetic dataset (run once; output is cached).

Two outputs, both written to evals/fixtures/synthetic/prompt_variants.json:

  paraphrases        3 rewordings of every routing case prompt (casual/terse, with a typo, more verbose),
                     validated so they keep exactly the names, times and facts of the original.
  creation_requests  For every agent-worthy topic, a natural message in which Sam first asks the assistant
                     to take on that job. Used by `run_baseline.py grow-roster` so OpenPoke names its own
                     agents instead of using the generator's names.

Uses the same model OpenPoke runs on (settings.interaction_agent_model) through OpenRouter.
Rerunning regenerates everything and will produce different text; commit the JSON to keep results comparable.

Usage (repo root): .venv/bin/python scripts/generate_prompt_variants.py [--only paraphrases|creation]
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES = REPO_ROOT / "evals" / "fixtures" / "synthetic"
OUT = FIXTURES / "prompt_variants.json"
sys.path.insert(0, str(REPO_ROOT))

from server.config import get_settings  # noqa: E402
from server.openrouter_client import request_chat_completion  # noqa: E402

PARAPHRASE_SYSTEM = """You rewrite chat messages that a busy insurance account manager (Sam) types to an AI assistant.
For each input message, write exactly 3 rewordings with the same meaning:
  1. terse and casual, like a quick text (lowercase is fine)
  2. natural but with one small typo or shorthand
  3. a bit longer and more polite, still one or two sentences

Hard rules:
- Keep every person and company name exactly as written. Never add a surname, company, or detail that is not in the original.
  If the original says only "Elena", the rewording must say only "Elena".
- Keep dates, times and weekdays exactly ("tomorrow at 9am" stays "tomorrow at 9am").
- Keep the request type: a question stays a question, a reminder stays a reminder, chit-chat stays chit-chat.
- Do not use quotation marks inside the rewordings.

Reply with JSON only: {"<id>": ["...", "...", "..."], ...}"""

CREATION_SYSTEM = """You write the first message an insurance account manager (Sam Rivera, Northbay Insurance Brokers, Toronto)
sends to an AI assistant to hand it a new piece of work. Each input describes one job.

For each job write one realistic message (1-2 sentences) in which Sam asks the assistant to take it on.
- Refer to people the way Sam naturally would: usually first name or full name, sometimes the company.
- Include one or two concrete details from the description so the job is clear.
- Do NOT copy the job title verbatim and do not invent a name for the task; just ask for the work.
- Vary the tone: some terse, some chatty.

Reply with JSON only: {"<id>": "...", ...}"""


def _parse_json(text: str) -> Dict[str, Any]:
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object in reply")
    return json.loads(text[start : end + 1])


async def _ask(system: str, payload: List[Dict[str, Any]], model: str, api_key: str) -> Dict[str, Any]:
    for attempt in range(3):
        try:
            response = await request_chat_completion(
                model=model, api_key=api_key, system=system,
                messages=[{"role": "user", "content": json.dumps(payload, ensure_ascii=False, indent=1)}],
            )
            return _parse_json(response["choices"][0]["message"]["content"] or "")
        except Exception as exc:
            if attempt == 2:
                print(f"  batch failed after retries: {exc}")
                return {}
            await asyncio.sleep(2 * (attempt + 1))
    return {}


_NAME_RE = re.compile(r"\b[A-Z][a-z]+(?:'[a-z]+)?\b")


def _names(text: str, known: set[str]) -> set[str]:
    """Capitalized tokens that are known person/company name parts."""
    return {tok.removesuffix("'s").lower() for tok in _NAME_RE.findall(text) if tok.removesuffix("'s").lower() in known}


def _valid_paraphrase(original: str, candidate: str, known: set[str]) -> Optional[str]:
    if not candidate or len(candidate) > 3 * len(original) + 80:
        return "length"
    lowered = candidate.lower()
    orig_names = {w.lower().removesuffix("'s") for w in re.findall(r"[A-Za-z']+", original) if w.lower().removesuffix("'s") in known}
    missing = [n for n in orig_names if n not in lowered]
    if missing:
        return f"dropped {missing}"
    added = _names(candidate, known) - orig_names
    if added:
        return f"added {sorted(added)}"
    for t in re.findall(r"\b\d{1,2}(?::\d{2})?\s?(?:am|pm)\b|\btomorrow\b|\b(?:monday|tuesday|wednesday|thursday|friday)\b", original.lower()):
        if t not in lowered:
            return f"dropped time '{t}'"
    return None


async def make_paraphrases(model: str, api_key: str, known: set[str]) -> Dict[str, List[str]]:
    cases = json.loads((FIXTURES / "routing_cases.json").read_text())["cases"]
    batches = [cases[i : i + 12] for i in range(0, len(cases), 12)]
    sem = asyncio.Semaphore(4)
    out: Dict[str, List[str]] = {}
    rejected: List[str] = []

    async def run(batch):
        async with sem:
            reply = await _ask(PARAPHRASE_SYSTEM, [{"id": c["id"], "message": c["prompt"]} for c in batch], model, api_key)
        for c in batch:
            keep = []
            for cand in (reply.get(c["id"]) or [])[:3]:
                reason = _valid_paraphrase(c["prompt"], str(cand).strip(), known)
                if reason:
                    rejected.append(f"{c['id']}: {reason}: {cand!r} (orig {c['prompt']!r})")
                else:
                    keep.append(str(cand).strip())
            out[c["id"]] = keep

    await asyncio.gather(*(run(b) for b in batches))
    print(f"paraphrases: {sum(map(len, out.values()))} kept for {len(out)} cases; {len(rejected)} rejected")
    for line in rejected[:15]:
        print("  rejected", line)
    return dict(sorted(out.items()))


async def make_creation_requests(model: str, api_key: str) -> Dict[str, str]:
    topics = [t for t in json.loads((FIXTURES / "topics.json").read_text())["topics"] if t["agent_worthy"]]
    jobs = [{"id": t["id"], "job": t["summary"], "people": t["people"], "client": t["client"]} for t in topics]
    batches = [jobs[i : i + 20] for i in range(0, len(jobs), 20)]
    sem = asyncio.Semaphore(4)
    out: Dict[str, str] = {}

    async def run(batch):
        async with sem:
            reply = await _ask(CREATION_SYSTEM, batch, model, api_key)
        for job in batch:
            text = str(reply.get(job["id"]) or "").strip()
            if text:
                out[job["id"]] = text

    await asyncio.gather(*(run(b) for b in batches))
    missing = [j["id"] for j in jobs if j["id"] not in out]
    if missing:
        print(f"creation: retrying {len(missing)} missing")
        await asyncio.gather(*(run([j]) for j in jobs if j["id"] in set(missing)))
    print(f"creation requests: {len(out)} of {len(jobs)} topics")
    return dict(sorted(out.items()))


async def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", choices=["paraphrases", "creation"], default=None)
    args = parser.parse_args()
    settings = get_settings()
    if not settings.openrouter_api_key:
        sys.exit("OPENROUTER_API_KEY is not set")
    model = settings.interaction_agent_model

    mailbox = json.loads((FIXTURES / "mailbox.json").read_text())
    topics = json.loads((FIXTURES / "topics.json").read_text())["topics"]
    known = {tok.lower() for c in mailbox["contacts"] for tok in re.findall(r"[A-Za-z']+", c["name"] + " " + c.get("organization", "")) if len(tok) > 2}
    known |= {tok.lower() for t in topics for p in t["people"] for tok in p.split() if len(tok) > 2}
    known -= {"the", "and", "inc", "ltd", "services", "insurance", "mutual", "general", "underwriting", "claims", "billing", "support", "security", "account"}

    existing = json.loads(OUT.read_text()) if OUT.exists() else {}
    result = {"model": model, **{k: v for k, v in existing.items() if k != "model"}}
    if args.only in (None, "paraphrases"):
        result["paraphrases"] = await make_paraphrases(model, settings.openrouter_api_key, known)
    if args.only in (None, "creation"):
        result["creation_requests"] = await make_creation_requests(model, settings.openrouter_api_key)
    OUT.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    asyncio.run(main())
