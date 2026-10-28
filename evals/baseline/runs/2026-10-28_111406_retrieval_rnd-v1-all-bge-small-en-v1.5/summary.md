# retrieval run 2026-10-28_111406 (rnd-v1-all-bge-small-en-v1.5)

git 42154b8 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 29.5s

Embedding model `BAAI/bge-small-en-v1.5`; prompts: all. Follow-up cases (reuse, lookalike, reminder) unless the column says otherwise. hit@k = correct agent in the top k; ambiguous_all@10 = every matching agent in the top 10; new_same_client@5 = for new jobs, the same client's other agent is in the top 5 (expected; the model must still create a new one).

### 40 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 69% | 87% | 92% | 96% | 0.77 | 69% | 75% | 65% | 100% | 81% | 60% |
| name | embedding | 70% | 88% | 92% | 93% | 0.78 | 70% | 75% | 75% | 100% | 69% | 41% |
| name | hybrid | 72% | 87% | 93% | 94% | 0.79 | 73% | 75% | 74% | 100% | 63% | 53% |
| name+first request | bm25 | 87% | 98% | 99% | 99% | 0.92 | 95% | 100% | 94% | 100% | 93% | 72% |
| name+first request | embedding | 84% | 95% | 96% | 99% | 0.89 | 83% | 98% | 76% | 100% | 80% | 47% |
| name+first request | hybrid | 86% | 97% | 99% | 100% | 0.91 | 96% | 100% | 89% | 100% | 95% | 69% |
| name+requests | bm25 | 87% | 98% | 99% | 99% | 0.92 | 95% | 100% | 94% | 100% | 93% | 72% |
| name+requests | embedding | 84% | 95% | 96% | 99% | 0.89 | 83% | 98% | 76% | 100% | 80% | 47% |
| name+requests | hybrid | 86% | 97% | 99% | 100% | 0.91 | 96% | 100% | 89% | 100% | 95% | 69% |
| name+requests+result | bm25 | 87% | 98% | 98% | 99% | 0.92 | 94% | 100% | 94% | 100% | 89% | 72% |
| name+requests+result | embedding | 81% | 93% | 95% | 98% | 0.87 | 82% | 100% | 68% | 100% | 92% | 40% |
| name+requests+result | hybrid | 88% | 97% | 99% | 100% | 0.92 | 96% | 100% | 88% | 100% | 96% | 63% |

### 500 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 52% | 71% | 84% | 86% | 0.60 | 43% | 65% | 54% | 100% | 19% | 55% |
| name | embedding | 42% | 62% | 72% | 80% | 0.52 | 31% | 65% | 24% | 79% | 5% | 12% |
| name | hybrid | 52% | 74% | 81% | 87% | 0.62 | 36% | 58% | 54% | 96% | 10% | 25% |
| name+first request | bm25 | 67% | 91% | 97% | 98% | 0.78 | 88% | 100% | 76% | 100% | 56% | 38% |
| name+first request | embedding | 66% | 83% | 86% | 89% | 0.74 | 62% | 90% | 42% | 89% | 12% | 14% |
| name+first request | hybrid | 71% | 93% | 94% | 97% | 0.81 | 78% | 98% | 71% | 100% | 49% | 20% |
| name+requests | bm25 | 67% | 91% | 97% | 98% | 0.78 | 88% | 100% | 76% | 100% | 56% | 38% |
| name+requests | embedding | 66% | 83% | 86% | 89% | 0.74 | 62% | 90% | 42% | 89% | 12% | 14% |
| name+requests | hybrid | 71% | 93% | 94% | 97% | 0.81 | 78% | 98% | 71% | 100% | 49% | 20% |
| name+requests+result | bm25 | 66% | 96% | 98% | 98% | 0.78 | 90% | 100% | 89% | 100% | 57% | 40% |
| name+requests+result | embedding | 60% | 81% | 85% | 89% | 0.70 | 52% | 85% | 42% | 64% | 28% | 12% |
| name+requests+result | hybrid | 69% | 92% | 95% | 98% | 0.79 | 79% | 100% | 68% | 89% | 51% | 26% |

