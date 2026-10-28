# retrieval run 2026-10-28_111602 (rnd-v1-all-mxbai-embed-large-v1)

git 42154b8 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 174.9s

Embedding model `mixedbread-ai/mxbai-embed-large-v1`; prompts: all. Follow-up cases (reuse, lookalike, reminder) unless the column says otherwise. hit@k = correct agent in the top k; ambiguous_all@10 = every matching agent in the top 10; new_same_client@5 = for new jobs, the same client's other agent is in the top 5 (expected; the model must still create a new one).

### 40 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 69% | 87% | 92% | 96% | 0.77 | 69% | 75% | 65% | 100% | 81% | 60% |
| name | embedding | 56% | 76% | 84% | 92% | 0.66 | 56% | 65% | 49% | 100% | 74% | 43% |
| name | hybrid | 64% | 84% | 90% | 94% | 0.73 | 59% | 75% | 64% | 100% | 71% | 53% |
| name+first request | bm25 | 87% | 98% | 99% | 99% | 0.92 | 95% | 100% | 94% | 100% | 93% | 72% |
| name+first request | embedding | 81% | 93% | 95% | 98% | 0.87 | 80% | 98% | 72% | 100% | 99% | 53% |
| name+first request | hybrid | 89% | 96% | 98% | 100% | 0.92 | 94% | 100% | 83% | 100% | 95% | 66% |
| name+requests | bm25 | 87% | 98% | 99% | 99% | 0.92 | 95% | 100% | 94% | 100% | 93% | 72% |
| name+requests | embedding | 81% | 93% | 95% | 98% | 0.87 | 80% | 98% | 72% | 100% | 99% | 53% |
| name+requests | hybrid | 89% | 96% | 98% | 100% | 0.92 | 94% | 100% | 83% | 100% | 95% | 66% |
| name+requests+result | bm25 | 87% | 98% | 98% | 99% | 0.92 | 94% | 100% | 94% | 100% | 89% | 72% |
| name+requests+result | embedding | 86% | 94% | 95% | 100% | 0.90 | 82% | 100% | 78% | 93% | 100% | 57% |
| name+requests+result | hybrid | 88% | 97% | 99% | 100% | 0.92 | 98% | 100% | 88% | 100% | 98% | 66% |

### 500 agents

| Profile | Method | hit@1 | hit@5 | hit@10 | hit@20 | mrr | opaque_hit@10 | lookalike_hit@1 | reminder_hit@5 | ambiguous_all@10 | multi_recall@20 | new_same_client@5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| name | bm25 | 52% | 71% | 84% | 86% | 0.60 | 43% | 65% | 54% | 100% | 19% | 55% |
| name | embedding | 43% | 59% | 67% | 74% | 0.51 | 30% | 60% | 32% | 32% | 25% | 18% |
| name | hybrid | 48% | 69% | 82% | 86% | 0.58 | 42% | 60% | 39% | 79% | 32% | 28% |
| name+first request | bm25 | 67% | 91% | 97% | 98% | 0.78 | 88% | 100% | 76% | 100% | 56% | 38% |
| name+first request | embedding | 62% | 81% | 85% | 89% | 0.70 | 53% | 92% | 39% | 61% | 43% | 35% |
| name+first request | hybrid | 70% | 92% | 94% | 96% | 0.80 | 76% | 98% | 71% | 100% | 57% | 36% |
| name+requests | bm25 | 67% | 91% | 97% | 98% | 0.78 | 88% | 100% | 76% | 100% | 56% | 38% |
| name+requests | embedding | 62% | 81% | 85% | 89% | 0.70 | 53% | 92% | 39% | 61% | 43% | 35% |
| name+requests | hybrid | 70% | 92% | 94% | 96% | 0.80 | 76% | 98% | 71% | 100% | 57% | 36% |
| name+requests+result | bm25 | 66% | 96% | 98% | 98% | 0.78 | 90% | 100% | 89% | 100% | 57% | 40% |
| name+requests+result | embedding | 65% | 83% | 87% | 90% | 0.74 | 58% | 92% | 40% | 36% | 48% | 28% |
| name+requests+result | hybrid | 75% | 92% | 96% | 98% | 0.83 | 84% | 98% | 72% | 93% | 57% | 35% |

