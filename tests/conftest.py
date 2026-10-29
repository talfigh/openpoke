"""Test setup: an isolated data dir before any server module computes its paths, plus shared fixtures."""

from __future__ import annotations

import os
import sys
import tempfile
import zlib
from pathlib import Path
from typing import Dict, List, Sequence

import numpy as np
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
os.environ["OPENPOKE_DATA_DIR"] = tempfile.mkdtemp(prefix="openpoke-tests-")
sys.path.insert(0, str(REPO_ROOT))

from server.services.execution.agent_search import tokenize  # noqa: E402
from server.services.execution.log_store import ExecutionAgentLogStore, _encode_payload  # noqa: E402
from server.services.execution.roster import AgentRoster  # noqa: E402


class FakeEmbedder:
    """Deterministic stand-in for the local model: a hashed bag of words, unit length. Records what it embeds."""

    def __init__(self, dims: int = 64):
        self.dims = dims
        self.embedded: List[str] = []

    def _vector(self, text: str) -> np.ndarray:
        vec = np.zeros(self.dims, dtype="float32")
        for tok in tokenize(text):
            vec[zlib.crc32(tok.encode()) % self.dims] += 1.0
        norm = np.linalg.norm(vec)
        return vec / norm if norm else vec

    def passages(self, texts: Sequence[str]) -> np.ndarray:
        self.embedded.extend(texts)
        return np.stack([self._vector(t) for t in texts])

    def query(self, text: str) -> np.ndarray:
        return self._vector(text)


class Workspace:
    """A roster and execution logs in a temporary folder, with log entries at chosen timestamps."""

    def __init__(self, root: Path):
        self.roster = AgentRoster(root / "roster.json")
        self.logs = ExecutionAgentLogStore(root / "execution_agents")

    def add(self, name: str, entries: List[tuple[str, str, str]]) -> None:
        """entries: (tag, "YYYY-MM-DD HH:MM:SS", text), oldest first."""
        self.roster.add_agent(name)
        with self.logs._log_path(name).open("a", encoding="utf-8") as handle:
            for tag, stamp, text in entries:
                handle.write(f'<{tag} timestamp="{stamp}">{_encode_payload(text)}</{tag}>\n')


@pytest.fixture
def workspace(tmp_path: Path) -> Workspace:
    return Workspace(tmp_path)


@pytest.fixture
def embedder() -> FakeEmbedder:
    return FakeEmbedder()


def agents(cards) -> List[str]:
    return [card.name for card in cards]


def entries_for(request: str, response: str = "", day: str = "2026-10-01") -> List[tuple[str, str, str]]:
    out = [("agent_request", f"{day} 09:00:00", request)]
    if response:
        out.append(("agent_response", f"{day} 09:05:00", response))
    return out


Pair = Dict[str, str]
