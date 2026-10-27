# Routing: generator vs OpenPoke agent names, original vs paraphrased prompts

Same 131 cases, same 40 core topics in every roster. "OpenPoke names" = the roster from `grow-roster` (`2026-10-27_130131_grow-roster_openpoke-names`), where OpenPoke named its own agents. Paraphrased = 3 validated rewordings per prompt (`fixtures/synthetic/prompt_variants.json`). Runs: `…routing_baseline{,-r2,-r3}`, `…134806_routing_paraphrases` and `…134806_routing_openpoke-names` (40 only; larger sizes failed on 402), `…150425_routing_{paraphrases,openpoke-names}-100-500`. Failed LLM calls are excluded (6 of ~2,700).

## Overall accuracy

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 74% | 75% | 70% | 59% |
| Generator names · paraphrased | 75% | 74% | 68% | 59% |
| OpenPoke names · original prompts | 72% | 70% | 62% | 59% |
| OpenPoke names · paraphrased | 71% | 73% | 64% | 58% |

## Accuracy: reuse

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 83% | 77% | 75% | 64% |
| Generator names · paraphrased | 82% | 77% | 76% | 67% |
| OpenPoke names · original prompts | 85% | 79% | 67% | 65% |
| OpenPoke names · paraphrased | 85% | 81% | 74% | 65% |

## Accuracy: lookalike

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 86% | 81% | 75% | 58% |
| Generator names · paraphrased | 78% | 67% | 69% | 56% |
| OpenPoke names · original prompts | 100% | 100% | 100% | 100% |
| OpenPoke names · paraphrased | 100% | 100% | 100% | 100% |

## Accuracy: reminder

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 47% | 60% | 47% | 38% |
| Generator names · paraphrased | 56% | 52% | 44% | 31% |
| OpenPoke names · original prompts | 30% | 20% | 15% | 15% |
| OpenPoke names · paraphrased | 27% | 27% | 15% | 13% |

## Accuracy: new

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 67% | 74% | 71% | 67% |
| Generator names · paraphrased | 66% | 76% | 67% | 67% |
| OpenPoke names · original prompts | 55% | 66% | 62% | 66% |
| OpenPoke names · paraphrased | 53% | 68% | 61% | 61% |

## Accuracy: ambiguous

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 81% | 86% | 62% | 14% |
| Generator names · paraphrased | 86% | 86% | 43% | 29% |
| OpenPoke names · original prompts | 86% | 86% | 57% | 29% |
| OpenPoke names · paraphrased | 86% | 86% | 67% | 19% |

## Duplicate created instead of reuse

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 22% | 24% | 27% | 37% |
| Generator names · paraphrased | 21% | 27% | 27% | 38% |
| OpenPoke names · original prompts | 25% | 32% | 36% | 37% |
| OpenPoke names · paraphrased | 24% | 26% | 32% | 38% |

## New job merged into an existing agent

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 33% | 26% | 29% | 33% |
| Generator names · paraphrased | 34% | 24% | 33% | 33% |
| OpenPoke names · original prompts | 45% | 34% | 38% | 34% |
| OpenPoke names · paraphrased | 46% | 32% | 39% | 39% |

## Reuse when the agent name doesn't mention the person in the prompt

| Condition | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| Generator names · original prompts (3 runs) | 28% | 26% | 22% | 20% |
| Generator names · paraphrased | 44% | 43% | 38% | 35% |
| OpenPoke names · original prompts | 36% | 32% | 25% | 18% |
| OpenPoke names · paraphrased | 43% | 42% | 36% | 30% |

