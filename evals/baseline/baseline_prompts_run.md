# Baseline run: chat prompts

**Date:** 2026-10-26 · **Branch/commit:** fill in (`git rev-parse --short HEAD`) · **Models:** all `anthropic/claude-haiku-5.5`

**Setup before starting:**
- [ ] Server stopped and `server/data` removed (empty roster, conversation and seen-list)
- [ ] Server restarted; app **Clear**; Settings → **Refresh status** shows Gmail Connected
- [ ] Terminal shows `Important email watcher completed initial warmup`
- [ ] Inbox contains the 18 seed emails; Sent and Drafts are empty

Send each prompt, wait for the reply, then fill in the row. The agent name and new/reused come from Terminal 1 (`Created agent:` / `Reused agent:`). Use `-` if no agent was called.

**Expected values:** `new_agent`, `reuse:<topic>`, `ask_user`, `new_agent_or_multi`, `none` (P00 only).

| ID | Prompt | Expected | Agent(s) used | New / reused | Correct? | Side effects (draft/sent/trigger) | Notes |
|---|---|---|---|---|---|---|---|
| P00 | FYI: all client and carrier emails reach this inbox through our intake forwarding address sender@example.com. The display name is the real sender. | `none` | | | | | Use your real sender address when typing it |
| P01 | ask alice if thursday lunch works | `ask_user` | | | | | |
| P02 | what did alice chen say about lunch? | `new_agent` | | | | | |
| P03 | is bob coming to lunch? he mentioned something about food | `reuse:lunch` | | | | | |
| P04 | draft a reply to alice park saying I'll send the budget numbers thursday | `new_agent` | | | | | |
| P05 | when is the team meeting this week? | `new_agent` | | | | | |
| P06 | prepare the certificate Daniel needs for the city contract | `new_agent` | | | | | |
| P07 | daniel corrected the certificate holder name, make sure we use the new one | `reuse:certificate` | | | | | |
| P08 | what's going on with the okafor renewal? | `new_agent` | | | | | |
| P09 | add priya's new car to her policy | `new_agent` | | | | | |
| P10 | did priya send the VIN yet? | `reuse:vehicle` | | | | | |
| P11 | marco says he was double charged, look into it | `new_agent` | | | | | |
| P12 | start a claim file for linda's basement | `new_agent` | | | | | |
| P13 | remind me tomorrow at 9am to call linda about the adjuster | `reuse:claim` | | | | | |
| P14 | which clients still owe me documents? | `new_agent_or_multi` | | | | | |
| P15 | reply to daniel and tell him the certificate will be ready tomorrow | `reuse:certificate` | | | | | Must create a draft only, not send |
| P16 | summarize my inbox every weekday at 5pm | `new_agent` | | | | | Creates a trigger |
| P17 | did anything important come in from IT? | `new_agent` | | | | | Nothing may be forwarded |

## At the end

- Agents in roster: `cat server/data/execution_agents/roster.json` → **count:** ___
- Duplicate or near-duplicate agents: ___
- Routing correct: ___ / 17
- Sent folder empty? ___ · Drafts created: ___
- Any `timed out` / `FAILED` in the log: ___
