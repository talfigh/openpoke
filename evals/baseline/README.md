# Baseline evidence (upstream OpenPoke behavior)

Captured on the `agent-overload` branch with only the setup fixes applied (retired model, Composio `link`, error logging). The overload solution is not applied here. The personal sender address is redacted to `sender@example.com`.

| File | What it shows |
|---|---|
| `2026-10-26_watcher_run_server_log.txt` | Server log after the 18 seed emails arrived, with no user prompts: agents created from alerts, duplicate concurrent runs, global batching, 90 s timeouts. |
| `2026-10-26_watcher_run_chat.txt` | What the user saw in the chat during the same run. |
| `Sent.png` | Test inbox Sent folder: empty. No email was sent or forwarded, including by the injection emails. |
| `Draft.png` / `linda_orphan_draft.txt` | A reply draft to Linda created by an agent run that then timed out. The user was never told about it. |
| `baseline_prompts_run.md` | Routing observations for prompts P00–P17 on a clean roster. |

Findings are summarized in `/NOTES.md`, sections 4 and 5.

## Offline baseline (synthetic inbox, 2026-10-27)

Produced by `evals/run_baseline.py` on `evals/fixtures/synthetic/`. Each run folder in `runs/` holds `results.json` (every case) and `summary.md`.

| File | What it shows |
|---|---|
| `routing_3runs.md` | Routing accuracy at 40/100/250/500 agents, mean and range over 3 runs. |
| `classifier_3runs.md` | Importance classifier over 3 runs. |
| `scenario_3runs.md` | 11-step end-to-end scenario over 3 runs. |
| `naming_and_paraphrase_comparison.md` | Generator vs OpenPoke-written agent names, original vs paraphrased prompts. |
| `naming_report.html` | The same comparison as a readable report with charts. |

Findings are in `/NOTES.md`, sections 6 and 7.
