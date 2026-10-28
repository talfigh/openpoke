"""Find the execution agents most relevant to a request: keyword (BM25) and embedding search over agent profiles."""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

DEFAULT_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
_RRF_K = 60  # standard reciprocal-rank-fusion constant

_TOKEN_RE = re.compile(r"[a-z0-9]+")
_STOPWORDS = {
    "a", "an", "and", "any", "are", "as", "at", "be", "been", "but", "by", "can", "could", "did", "do", "does", "for",
    "from", "get", "got", "had", "has", "have", "her", "his", "i", "if", "in", "into", "is", "it", "its", "just", "let",
    "me", "my", "of", "on", "or", "our", "please", "she", "so", "that", "the", "their", "them", "then", "there", "they",
    "this", "to", "up", "us", "was", "we", "were", "what", "when", "where", "whether", "which", "who", "will", "with",
    "yet", "you", "your",
}


def tokenize(text: str) -> List[str]:
    """Lowercase word tokens without stopwords, single letters ("farah's" -> "farah") or a plural "s"."""
    tokens = []
    for tok in _TOKEN_RE.findall(text.lower()):
        if len(tok) < 2 or tok in _STOPWORDS:
            continue
        if len(tok) > 3 and tok.endswith("s") and not tok.endswith("ss"):
            tok = tok[:-1]
        tokens.append(tok)
    return tokens


def build_profile(name: str, entries: Iterable[Tuple[str, str]], *, requests: int = 10, responses: int = 1) -> str:
    """Searchable text for an agent: its name, first request (its purpose), latest requests and latest results.

    `entries` are (tag, text) pairs from the execution log, oldest first.
    """
    entries = list(entries)
    reqs = [text for tag, text in entries if tag == "agent_request"]
    resps = [text for tag, text in entries if tag == "agent_response"]
    picked = (reqs[:1] + reqs[1:][-(requests - 1):]) if requests > 1 else reqs[:requests]
    return "\n".join([name, *picked, *(resps[-responses:] if responses else [])])


class BM25:
    """Okapi BM25 over pre-tokenized documents."""

    def __init__(self, docs: Sequence[List[str]], k1: float = 1.5, b: float = 0.75):
        self._k1, self._b = k1, b
        self._tf = [Counter(doc) for doc in docs]
        self._len = [len(doc) for doc in docs]
        self._avg = (sum(self._len) / len(docs)) if docs else 0.0
        df = Counter(tok for doc in docs for tok in set(doc))
        n = len(docs)
        self._idf = {tok: math.log(1 + (n - f + 0.5) / (f + 0.5)) for tok, f in df.items()}

    def scores(self, query: List[str]) -> List[float]:
        out = []
        for tf, length in zip(self._tf, self._len):
            norm = self._k1 * (1 - self._b + self._b * length / self._avg) if self._avg else self._k1
            out.append(sum(self._idf.get(t, 0.0) * tf[t] * (self._k1 + 1) / (tf[t] + norm) for t in query if t in tf))
        return out


class Embedder:
    """Local sentence embeddings (fastembed, ONNX). Loaded on first use; vectors are unit length."""

    def __init__(self, model_name: str = DEFAULT_EMBEDDING_MODEL):
        self.model_name = model_name
        self._model = None

    def _load(self):
        if self._model is None:
            from fastembed import TextEmbedding

            self._model = TextEmbedding(self.model_name)
        return self._model

    def passages(self, texts: Sequence[str]):
        import numpy as np

        return np.array(list(self._load().passage_embed(list(texts))), dtype="float32")

    def query(self, text: str):
        import numpy as np

        return np.array(next(iter(self._load().query_embed(text))), dtype="float32")


class AgentSearch:
    """Ranks agents for a query by BM25, embedding cosine similarity, or both fused by reciprocal rank."""

    def __init__(self, embedder: Optional[Embedder] = None):
        self._embedder = embedder
        self._names: List[str] = []
        self._bm25: Optional[BM25] = None
        self._vectors = None

    def index(self, profiles: Dict[str, str], vectors=None) -> None:
        """Index name -> profile text. Precomputed `vectors` (same order) skip embedding."""
        self._names = list(profiles)
        self._bm25 = BM25([tokenize(text) for text in profiles.values()])
        if self._embedder is not None:
            self._vectors = vectors if vectors is not None else self._embedder.passages(list(profiles.values()))

    def search(self, query: str, k: int = 10, method: str = "hybrid") -> List[Tuple[str, float]]:
        """Top-k (name, score). Scores are BM25 points, cosine similarity, or RRF points depending on `method`."""
        if not self._names:
            return []
        if method == "bm25":
            ranked = self._rank(self._bm25.scores(tokenize(query)))
        elif method == "embedding":
            ranked = self._rank(self._cosine(query))
        elif method == "hybrid":
            fused: Dict[int, float] = {}
            for ranking in (self._rank(self._bm25.scores(tokenize(query))), self._rank(self._cosine(query))):
                for pos, (idx, _) in enumerate(ranking):
                    fused[idx] = fused.get(idx, 0.0) + 1.0 / (_RRF_K + pos + 1)
            ranked = sorted(fused.items(), key=lambda item: -item[1])
        else:
            raise ValueError(f"unknown search method: {method}")
        return [(self._names[idx], round(float(score), 4)) for idx, score in ranked[:k]]

    def _cosine(self, query: str) -> List[float]:
        if self._embedder is None or self._vectors is None:
            raise ValueError("embedding search needs an Embedder")
        return list(self._vectors @ self._embedder.query(query))

    @staticmethod
    def _rank(scores: List[float]) -> List[Tuple[int, float]]:
        return sorted(enumerate(scores), key=lambda item: -item[1])
