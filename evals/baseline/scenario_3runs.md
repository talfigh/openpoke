# scenario: 3 runs

Runs: 2026-10-27_130417_scenario_baseline-r1, 2026-10-27_130805_scenario_baseline-r2, 2026-10-27_131429_scenario_baseline-r3

Each cell is mean (min–max) across runs.

| Metric | Value |
|---|---|
| Steps passed | 8.67 (7.00–10.00) |
| Agents created | 2.00 (1.00–3.00) |
| Execution failures | 1.00 (0.00–2.00) |
| Execution timeouts | 1.00 (0.00–2.00) |
| Agent runs from email alone | 0.33 (0.00–1.00) |
| Duplicate replies | 0.00 (0.00–0.00) |
| Sends/forwards | 0.33 (0.00–1.00) |
| Cost $ | 0.13 (0.09–0.16) |

| Step | Passed | Time s | Failed checks seen |
|---|---|---|---|
| S01 what's the latest on linda's basement claim? | 3/3 | 26.90 (25.60–28.70) |  |
| S02 what's going on with the okafor renewal? | 0/3 | 33.57 (32.40–34.90) | forbid, min_new_agents |
| S03 remind me tomorrow at 9am to call linda about the  | 1/3 | 9.37 (8.40–10.00) | reuse, trigger_for |
| S04 draft a reply to alice park saying I'll send the b | 2/3 | 19.73 (16.80–22.90) | no_send |
| S05 deliver | 3/3 | 33.97 (32.40–35.30) |  |
| S06 did anything important come in from IT? | 3/3 | 9.70 (2.50–23.80) |  |
| S07 reply to daniel and tell him the certificate will  | 2/3 | 11.27 (6.60–13.70) | reuse |
| S08 ask alice if thursday lunch works | 3/3 | 18.67 (17.70–19.30) |  |
| S09 which clients still owe me documents? | 3/3 | 164 (45.30–282) |  |
| S10 marco says he was double charged, look into it | 3/3 | 29.67 (25.50–36.00) |  |
| S11 thanks, that's all for now | 3/3 | 2.27 (1.70–2.80) |  |
