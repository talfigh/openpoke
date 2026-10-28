# retrieval run 2026-10-28_111436 (rnd-v1-all-bge-base-en-v1.5)

git 42154b8 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 85.8s

Embedding model `BAAI/bge-base-en-v1.5`; prompts: all. Follow-up cases (reuse, lookalike, reminder) unless the column says otherwise. hit@k = correct agent in the top k; ambiguous_all@10 = every matching agent in the top 10; new_same_client@5 = for new jobs, the same client's other agent is in the top 5 (expected; the model must still create a new one).

### 40 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 69% | 87% | 92% | 96% | 0.77 | 69% | 75% | 65% | 100% | 81% | 60% |
| name | embedding | 64% | 84% | 89% | 94% | 0.73 | 56% | 79% | 60% | 100% | 53% | 38% |
| name | hybrid | 70% | 88% | 93% | 94% | 0.79 | 73% | 81% | 74% | 100% | 67% | 52% |
| name+first request | bm25 | 87% | 98% | 99% | 99% | 0.92 | 95% | 100% | 94% | 100% | 93% | 72% |
| name+first request | embedding | 83% | 93% | 93% | 98% | 0.88 | 76% | 98% | 75% | 100% | 100% | 57% |
| name+first request | hybrid | 87% | 96% | 98% | 99% | 0.91 | 90% | 100% | 88% | 100% | 99% | 69% |
| name+requests | bm25 | 87% | 98% | 99% | 99% | 0.92 | 95% | 100% | 94% | 100% | 93% | 72% |
| name+requests | embedding | 83% | 93% | 93% | 98% | 0.88 | 76% | 98% | 75% | 100% | 100% | 57% |
| name+requests | hybrid | 87% | 96% | 98% | 99% | 0.91 | 90% | 100% | 88% | 100% | 99% | 69% |
| name+requests+result | bm25 | 87% | 98% | 98% | 99% | 0.92 | 94% | 100% | 94% | 100% | 89% | 72% |
| name+requests+result | embedding | 83% | 93% | 95% | 97% | 0.87 | 83% | 100% | 76% | 100% | 95% | 51% |
| name+requests+result | hybrid | 87% | 96% | 98% | 99% | 0.92 | 94% | 100% | 86% | 100% | 98% | 69% |

### 500 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 52% | 71% | 84% | 86% | 0.60 | 43% | 65% | 54% | 100% | 19% | 55% |
| name | embedding | 44% | 61% | 66% | 75% | 0.52 | 28% | 67% | 32% | 64% | 12% | 15% |
| name | hybrid | 49% | 71% | 79% | 85% | 0.59 | 31% | 67% | 39% | 93% | 17% | 27% |
| name+first request | bm25 | 67% | 91% | 97% | 98% | 0.78 | 88% | 100% | 76% | 100% | 56% | 38% |
| name+first request | embedding | 67% | 85% | 88% | 92% | 0.75 | 67% | 96% | 51% | 46% | 28% | 23% |
| name+first request | hybrid | 76% | 93% | 93% | 95% | 0.83 | 75% | 100% | 74% | 100% | 56% | 28% |
| name+requests | bm25 | 67% | 91% | 97% | 98% | 0.78 | 88% | 100% | 76% | 100% | 56% | 38% |
| name+requests | embedding | 67% | 85% | 88% | 92% | 0.75 | 67% | 96% | 51% | 46% | 28% | 23% |
| name+requests | hybrid | 76% | 93% | 93% | 95% | 0.83 | 75% | 100% | 74% | 100% | 56% | 28% |
| name+requests+result | bm25 | 66% | 96% | 98% | 98% | 0.78 | 90% | 100% | 89% | 100% | 57% | 40% |
| name+requests+result | embedding | 71% | 85% | 87% | 91% | 0.77 | 67% | 92% | 46% | 36% | 14% | 22% |
| name+requests+result | hybrid | 75% | 93% | 94% | 97% | 0.83 | 80% | 100% | 75% | 96% | 51% | 29% |

