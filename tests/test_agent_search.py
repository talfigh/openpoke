"""Keyword, embedding and hybrid search over agent profiles (server/services/execution/agent_search.py)."""

import numpy as np
import pytest

from server.services.execution.agent_search import BM25, AgentSearch, build_profile, tokenize


def test_tokenize_lowercases_and_drops_stopwords_and_single_letters():
    assert tokenize("Did Farah's renewal figures arrive yet?") == ["farah", "renewal", "figure", "arrive"]


def test_tokenize_keeps_short_names_and_double_s():
    assert tokenize("Al asked Ross") == ["al", "asked", "ross"]


@pytest.mark.xfail(reason="'will' is a stopword, so a client named Will is dropped from the query (known gap)")
def test_tokenize_keeps_the_name_will():
    assert "will" in tokenize("Will Chen renewal")


def test_profile_has_name_first_request_latest_requests_and_latest_result():
    entries = [("agent_request", f"request {i}") for i in range(12)] + [
        ("agent_response", "old result"),
        ("agent_action", "tool call, not part of the profile"),
        ("agent_response", "latest result"),
    ]
    lines = build_profile("Certificate for Maya", entries).splitlines()
    assert lines == ["Certificate for Maya", "request 0"] + [f"request {i}" for i in range(3, 12)] + ["latest result"]


def test_profile_of_a_name_only():
    assert build_profile("Lunch", [("agent_request", "book a table")], requests=0, responses=0) == "Lunch"


def test_bm25_ranks_a_rare_shared_word_above_a_common_one():
    docs = [tokenize("renewal for farah"), tokenize("renewal for daniel"), tokenize("renewal for maya")]
    scores = BM25(docs).scores(tokenize("farah renewal"))
    assert scores.index(max(scores)) == 0
    assert BM25(docs).scores(tokenize("bakery"))[0] == 0.0


def test_keyword_search_finds_an_agent_whose_name_hides_the_person():
    search = AgentSearch()
    search.index({
        "MacLeod Print Shop Ltd. COI": "MacLeod Print Shop Ltd. COI\nRequest a certificate of insurance. Find Ana's email for details.",
        "Certificate for Maya Cardenas": "Certificate for Maya Cardenas\nRequest a certificate for Cardenas Bakery.",
    })
    assert search.search("where are we on Ana's certificate?", k=1, method="bm25")[0][0] == "MacLeod Print Shop Ltd. COI"


class ScriptedEmbedder:
    """Embeddings that deliberately disagree with keyword search: the query points at agent B."""

    def passages(self, texts):
        return np.array([[0.0, 1.0], [1.0, 0.0], [0.6, 0.8]], dtype="float32")[: len(texts)]

    def query(self, text):
        return np.array([1.0, 0.0], dtype="float32")


def _disagreeing_search():
    search = AgentSearch(ScriptedEmbedder())
    search.index({"A": "farah renewal tran roofing", "B": "office party", "C": "team lunch"})
    return search


def test_hybrid_trusts_keyword_ranking_three_to_one():
    assert _disagreeing_search().search("farah renewal", k=1, method="hybrid")[0][0] == "A"


def test_hybrid_follows_embeddings_when_keyword_weight_is_tiny():
    assert _disagreeing_search().search("farah renewal", k=1, method="hybrid", bm25_weight=0.01)[0][0] == "B"


def test_unknown_method_and_missing_embedder_are_errors():
    with pytest.raises(ValueError):
        _disagreeing_search().search("x", method="magic")
    keyword_only = AgentSearch()
    keyword_only.index({"A": "a"})
    with pytest.raises(ValueError):
        keyword_only.search("a", method="embedding")
