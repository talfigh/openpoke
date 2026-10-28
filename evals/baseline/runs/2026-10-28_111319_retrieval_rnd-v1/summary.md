# retrieval run 2026-10-28_111319 (rnd-v1)

git 42154b8 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 13.5s

Embedding model `BAAI/bge-small-en-v1.5`. Follow-up cases (reuse, lookalike, reminder) unless the column says otherwise. hit@k = correct agent in the top k; ambiguous_all@10 = every matching agent in the top 10; new_same_client@5 = for new jobs, the same client's other agent is in the top 5 (expected; the model must still create a new one).

### 40 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 69% | 87% | 93% | 96% | 0.77 | 67% | 75% | 65% | 100% | 81% | 59% |
| name | embedding | 71% | 87% | 93% | 93% | 0.79 | 67% | 67% | 75% | 100% | 72% | 41% |
| name | hybrid | 71% | 87% | 94% | 94% | 0.79 | 72% | 75% | 75% | 100% | 61% | 55% |
| name+first request | bm25 | 87% | 98% | 99% | 100% | 0.92 | 94% | 100% | 95% | 100% | 100% | 72% |
| name+first request | embedding | 83% | 94% | 95% | 99% | 0.89 | 78% | 100% | 75% | 100% | 83% | 48% |
| name+first request | hybrid | 86% | 98% | 100% | 100% | 0.91 | 100% | 100% | 90% | 100% | 100% | 69% |
| name+requests | bm25 | 87% | 98% | 99% | 100% | 0.92 | 94% | 100% | 95% | 100% | 100% | 72% |
| name+requests | embedding | 83% | 94% | 95% | 99% | 0.89 | 78% | 100% | 75% | 100% | 83% | 48% |
| name+requests | hybrid | 86% | 98% | 100% | 100% | 0.91 | 100% | 100% | 90% | 100% | 100% | 69% |
| name+requests+result | bm25 | 87% | 98% | 99% | 100% | 0.93 | 94% | 100% | 95% | 100% | 100% | 72% |
| name+requests+result | embedding | 80% | 92% | 94% | 98% | 0.86 | 78% | 100% | 65% | 100% | 100% | 38% |
| name+requests+result | hybrid | 87% | 98% | 99% | 100% | 0.92 | 94% | 100% | 90% | 100% | 100% | 62% |

### 500 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 54% | 71% | 83% | 86% | 0.62 | 33% | 67% | 55% | 100% | 25% | 52% |
| name | embedding | 45% | 64% | 73% | 80% | 0.55 | 17% | 67% | 25% | 86% | 12% | 14% |
| name | hybrid | 54% | 74% | 81% | 86% | 0.63 | 22% | 58% | 55% | 100% | 17% | 31% |
| name+first request | bm25 | 69% | 92% | 98% | 98% | 0.79 | 89% | 100% | 80% | 100% | 72% | 38% |
| name+first request | embedding | 68% | 83% | 86% | 89% | 0.75 | 61% | 92% | 40% | 86% | 0% | 14% |
| name+first request | hybrid | 71% | 93% | 94% | 98% | 0.81 | 72% | 100% | 70% | 100% | 62% | 17% |
| name+requests | bm25 | 69% | 92% | 98% | 98% | 0.79 | 89% | 100% | 80% | 100% | 72% | 38% |
| name+requests | embedding | 68% | 83% | 86% | 89% | 0.75 | 61% | 92% | 40% | 86% | 0% | 14% |
| name+requests | hybrid | 71% | 93% | 94% | 98% | 0.81 | 72% | 100% | 70% | 100% | 62% | 17% |
| name+requests+result | bm25 | 67% | 98% | 98% | 98% | 0.79 | 89% | 100% | 95% | 100% | 56% | 41% |
| name+requests+result | embedding | 62% | 81% | 82% | 88% | 0.72 | 39% | 83% | 40% | 71% | 28% | 14% |
| name+requests+result | hybrid | 70% | 92% | 94% | 99% | 0.79 | 72% | 100% | 70% | 86% | 58% | 24% |

