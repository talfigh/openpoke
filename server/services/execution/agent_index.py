"""Searchable view of the agent roster, so the interaction agent sees the relevant agents instead of all of them."""

from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from ...logging_config import logger
from .agent_search import AgentSearch, Embedder, build_profile, tokenize
from .log_store import ExecutionAgentLogStore, get_execution_agent_logs
from .roster import AgentRoster, get_agent_roster

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
_SNIPPET_CHARS = 180


@dataclass
class AgentCard:
    """What the interaction agent sees about one agent."""

    name: str
    purpose: str
    latest: str
    last_active: str

    def to_payload(self) -> Dict[str, str]:
        return {"name": self.name, "purpose": self.purpose, "latest": self.latest, "last_active": self.last_active}


def _snippet(text: str) -> str:
    text = " ".join(text.split())
    return text if len(text) <= _SNIPPET_CHARS else text[: _SNIPPET_CHARS - 1] + "…"


class AgentIndex:
    """Builds agent profiles from the execution logs on demand and ranks them for a query.

    Profiles change whenever an agent gets a new request or finishes a run; embeddings are cached by profile text,
    so only changed agents are re-embedded on the next search.
    """

    def __init__(self, roster: AgentRoster, logs: ExecutionAgentLogStore, embedder: Optional[Embedder] = None):
        self._roster = roster
        self._logs = logs
        self._embedder = embedder
        self._vectors: Dict[str, Any] = {}  # profile text -> embedding
        self._lock = threading.Lock()

    def _entries(self) -> Dict[str, List[Tuple[str, str, str]]]:
        self._roster.load()
        return {name: list(self._logs.iter_entries(name)) for name in self._roster.get_agents()}

    @staticmethod
    def _card(name: str, entries: List[Tuple[str, str, str]]) -> AgentCard:
        requests = [payload for tag, _, payload in entries if tag == "agent_request"]
        responses = [payload for tag, _, payload in entries if tag == "agent_response"]
        latest = responses[-1] if responses else (requests[-1] if len(requests) > 1 else "")
        last_active = max((ts for _, ts, _ in entries if ts), default="")[:10]
        return AgentCard(name, _snippet(requests[0]) if requests else "", _snippet(latest), last_active)

    def _embed_missing(self, profiles: List[str]) -> Optional[List[Any]]:
        if self._embedder is None:
            return None
        with self._lock:
            missing = [p for p in dict.fromkeys(profiles) if p not in self._vectors]
            if missing:
                try:
                    self._vectors.update(zip(missing, self._embedder.passages(missing)))
                except Exception as exc:  # e.g. fastembed missing or model download failed
                    logger.warning(f"Agent embeddings unavailable, using keyword search only: {exc}")
                    self._embedder = None
                    return None
            vectors = [self._vectors[p] for p in profiles]
            if len(self._vectors) > 2 * len(profiles):  # drop embeddings of profiles that have since changed
                self._vectors = dict(zip(profiles, vectors))
            return vectors

    def search(self, query: str, k: int = 10, entries: Optional[Dict[str, List[Tuple[str, str, str]]]] = None) -> List[AgentCard]:
        """Agents most relevant to `query`, best first. `entries` reuses logs already read for this turn."""
        entries = self._entries() if entries is None else entries
        if not entries or not query.strip():
            return []
        names = list(entries)
        profiles = [build_profile(n, [(tag, payload) for tag, _, payload in entries[n]]) for n in names]
        vectors = self._embed_missing(profiles)
        search = AgentSearch(self._embedder if vectors is not None else None)
        if vectors is not None:
            import numpy as np

            search.index(dict(zip(names, profiles)), vectors=np.stack(vectors))
        else:
            search.index(dict(zip(names, profiles)))
        ranked = search.search(query, k=k, method="hybrid" if vectors is not None else "bm25")
        return [self._card(name, entries[name]) for name, _ in ranked]

    def recent(self, n: int = 5, entries: Optional[Dict[str, List[Tuple[str, str, str]]]] = None) -> List[AgentCard]:
        """Most recently active agents by their newest log entry (ties: most recently added first)."""
        entries = self._entries() if entries is None else entries
        order = {name: i for i, name in enumerate(entries)}
        newest = sorted(entries, key=lambda name: (max((ts for _, ts, _ in entries[name] if ts), default=""), order[name]), reverse=True)
        return [self._card(name, entries[name]) for name in newest[:n]]

    def candidates(self, message: str, context: str = "", k: int = 10, k_context: int = 3, recent: int = 5) -> List[AgentCard]:
        """Agents to show for one turn, without repeats: the top `k` for the message, the top `k_context` for the
        recent conversation, then the `recent` most recently active agents.

        A message with almost nothing to search for ("okay", "do it") gives its slots to the conversation search;
        the conversation search also covers replies like "yes send it" whose words don't name the work.
        """
        entries = self._entries()
        if len(tokenize(message)) < 2:
            k, k_context = 0, k + k_context
        groups = [
            self.search(message, k=k, entries=entries) if k else [],
            self.search(f"{context}\n{message}", k=k_context, entries=entries) if context.strip() else [],
            self.recent(recent, entries=entries),
        ]
        shown: Dict[str, AgentCard] = {}
        for group in groups:
            for card in group:
                shown.setdefault(card.name, card)
        return list(shown.values())

    def size(self) -> int:
        self._roster.load()
        return len(self._roster.get_agents())


_agent_index: Optional[AgentIndex] = None


def get_agent_index() -> AgentIndex:
    global _agent_index
    if _agent_index is None:
        _agent_index = AgentIndex(get_agent_roster(), get_execution_agent_logs(), Embedder(EMBEDDING_MODEL))
    return _agent_index
