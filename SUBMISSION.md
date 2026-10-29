# Agent overload in OpenPoke: submission

**Branch:** `agent-overload`. **Baseline tag:** `baseline-v1` (upstream behaviour, measured before any fix). Details and every number's source: [`NOTES.md`](NOTES.md) sections 6–9.

## The problem

The Interaction Agent sees every execution agent as a bare name, `<agent name="…"/>`, in every prompt, and reuses an agent only if it types an existing name exactly. As the roster grows, it creates duplicates and loses work whose name doesn't mention the person ("Ana's certificate" → *MacLeod Print Shop Ltd. COI*).

## How it was tested

No real inbox is needed. A fake Gmail backend (`server/services/gmail/fake_backend.py`, `OPENPOKE_FAKE_GMAIL`) answers every Composio call from a synthetic broker mailbox (995 emails, 90 days); writes go to an outbox file, nothing is sent. `OPENPOKE_DATA_DIR` isolates each run.

| Eval (`evals/run_baseline.py`) | What it checks |
|---|---|
| `routing` | 131 labelled chat messages against rosters of 40–500 agents; the real Interaction Agent decides, dispatch is intercepted. Scores reuse, duplicates, wrong agent, new-job merges, ambiguous names, reminders. Writes `failures.md` per run. |
| `retrieval` | Offline, no LLM: where the correct agent ranks under each search method and profile. |
| `scenario` | The whole app end to end: 11 chat and email steps with checks on routing, reminders and the outbox. |
| `classifier` | The importance watcher on 222 labelled emails, including scam warnings. |

Baselines were repeated 3 times (overall accuracy varies about ±2 points). Data: `scripts/generate_synthetic_dataset.py` (deterministic) and `scripts/generate_prompt_variants.py`.

## The fix: search agents, show only the relevant ones

`OPENPOKE_AGENT_ROSTER=search` (default `all` keeps upstream behaviour for comparison).

- **Profiles** (`server/services/execution/agent_search.py`): each agent's name + first instruction + last 9 instructions + latest result, built from the logs OpenPoke already writes.
- **Search**: keyword (BM25) and local embeddings (`fastembed`, bge-base), fused with keyword weighted 3:1. Offline, keyword search on profiles puts the right agent in the top 10 for 98% of follow-ups at 500 agents, against 83% with names alone and 86–88% for embeddings alone.
- **Cards** (`server/services/execution/agent_index.py`): each turn the model sees up to 18 agents (10 for the message, 3 for the recent conversation, 5 most recently active) with purpose, latest status and last-active date, plus prompt rules: reuse only for the same person and job; cards are for choosing, not answering.
- **Freshness**: embeddings are cached by profile text, so only changed agents are re-embedded; the server embeds all agents in the background at startup and never blocks a search on it.

## Results (baseline: mean of 3 runs · after: final code)

| | 40 agents | 500 agents |
|---|---|---|
| Overall routing accuracy | 74% → **91%** | 59% → **86%** |
| Follow-up reaches the right agent | 75% → **96%** | 57% → **93%** |
| Follow-up creates a duplicate | 22% → **1%** | 37% → **4%** |
| Name hides the person | 28% → **89%** | 20% → **78%** |
| Prompt tokens per message | 5.8k → 7.6k | 16.1k → **7.3k** |
| End-to-end scenario (100 agents) | | 8.7 → **10 / 11** steps |

Each change was tested one at a time (v1–v4 and an ablation that removed a search tool); see the commits and NOTES 8.

## Other gaps found

| Gap | Status |
|---|---|
| Scam emails dropped silently by the importance classifier (6–7 of 12 warned) | **Fixed**: one prompt sentence, 12 of 12 warned (NOTES 9) |
| First message after restart blocked the server while embedding | **Fixed**: background warm-up |
| `Optional` used but never imported in the log store | **Fixed** |
| An execution agent sent a reply without approval (`gmail_reply_to_thread`, 1 of 3 runs) | Open (NOTES 7.2) |
| Agents created from email alerts alone; same agent running twice at once; one global batch delays results | Open (NOTES 4) |
| Every completion reserves 65k output tokens (no `max_tokens`) | Open (NOTES 1.3) |

**Limits:** one run per R&D version; prompt rules were tuned on the same 131 messages; 7 of 131 cases have labelling mistakes (flagged, NOTES 7.10); confirmations, nicknames and long agent histories aren't in the test set yet.

## Run it

```bash
pip install -r server/requirements.txt          # in a Python 3.10+ venv; .env with OPENROUTER_API_KEY

# Evals (routing costs about $0.30 per roster size)
python evals/run_baseline.py retrieval                                   # free
python evals/run_baseline.py routing --sizes 40 500                      # upstream behaviour
python evals/run_baseline.py routing --sizes 40 500 --agent-roster search
python evals/run_baseline.py scenario --agent-roster search

# The app with 500 existing agents and the fake inbox (nothing is sent)
python scripts/seed_demo_data.py --size 500 --data-dir /tmp/openpoke-demo
OPENPOKE_FAKE_GMAIL=evals/fixtures/synthetic/mailbox.json OPENPOKE_DATA_DIR=/tmp/openpoke-demo \
  OPENPOKE_AGENT_ROSTER=search python -m server.server
npm run dev --prefix web                                                  # then open http://localhost:3000
```
