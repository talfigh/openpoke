"""Cards, candidates, recency, the embedding cache and fallbacks (server/services/execution/agent_index.py)."""

import time

from server.services.execution.agent_index import AgentIndex

from conftest import agents, entries_for


def _broker_roster(workspace):
    workspace.add("Linda Gauthier Water Claim", entries_for(
        "Help Linda Gauthier with her basement water claim; find the adjuster.", "Adjuster assigned, waiting on photos.", "2026-09-01"))
    workspace.add("Priya Sharma Auto Policy", entries_for(
        "Add Priya Sharma's Honda CR-V to her auto policy; get the VIN.", "Waiting on the VIN.", "2026-09-02"))
    workspace.add("Certificate for Maya Cardenas", entries_for(
        "Request a certificate of insurance for Cardenas Bakery. Find Maya's email.", "", "2026-09-03"))
    for i in range(6):
        workspace.add(f"Filler {i}", entries_for(f"Unrelated job number {i} about newsletters.", "", "2026-01-0{}".format(i + 1)))
    workspace.add("Lunch with Alice and Bob", entries_for("Book Thursday lunch with Alice Chen and Bob.", "", "2026-10-20"))


def test_card_shows_first_request_latest_result_and_date(workspace):
    workspace.add("Claim", [
        ("agent_request", "2026-10-01 09:00:00", "Open the claim"),
        ("agent_request", "2026-10-02 09:00:00", "Ask for photos"),
        ("agent_response", "2026-10-02 09:05:00", "Photos requested"),
    ])
    card = AgentIndex(workspace.roster, workspace.logs).search("claim photos", k=1)[0]
    assert (card.name, card.purpose, card.latest, card.last_active) == ("Claim", "Open the claim", "Photos requested", "2026-10-02")


def test_card_shows_the_latest_request_while_no_result_exists_and_truncates(workspace):
    workspace.add("Quote", [("agent_request", "2026-10-01 09:00:00", "x" * 300), ("agent_request", "2026-10-02 09:00:00", "Follow up")])
    card = AgentIndex(workspace.roster, workspace.logs).search("follow up", k=1)[0]
    assert card.latest == "Follow up"
    assert len(card.purpose) == 180 and card.purpose.endswith("…")


def test_message_matches_come_first_without_repeats(workspace, embedder):
    _broker_roster(workspace)
    cards = AgentIndex(workspace.roster, workspace.logs, embedder).candidates(
        "did priya send the VIN yet?", context="earlier chat about Linda's basement", k=3, k_context=2, recent=2)
    names = agents(cards)
    assert names[0] == "Priya Sharma Auto Policy"
    assert len(names) == len(set(names))
    assert "Lunch with Alice and Bob" in names  # most recently active


def test_okay_gives_every_slot_to_the_conversation_search(workspace, embedder):
    _broker_roster(workspace)
    context = "Poke: Linda's adjuster wants basement photos. Want me to send her a reply?"
    cards = AgentIndex(workspace.roster, workspace.logs, embedder).candidates("okay", context=context, k=3, k_context=1, recent=0)
    assert agents(cards)[0] == "Linda Gauthier Water Claim"
    assert len(cards) == 4  # k + k_context slots, all from the conversation search


def test_recent_orders_by_newest_log_entry(workspace):
    workspace.add("Old", entries_for("old work", "", "2025-01-01"))
    workspace.add("Newest", entries_for("new work", "", "2026-10-28"))
    workspace.add("Middle", entries_for("middle work", "", "2026-06-01"))
    assert agents(AgentIndex(workspace.roster, workspace.logs).recent(2)) == ["Newest", "Middle"]


def test_only_changed_profiles_are_embedded_again(workspace, embedder):
    _broker_roster(workspace)
    index = AgentIndex(workspace.roster, workspace.logs, embedder)
    index.search("priya vin")
    first = len(embedder.embedded)
    index.search("linda adjuster")
    assert len(embedder.embedded) == first  # nothing changed, everything cached
    workspace.logs.record_agent_response("Priya Sharma Auto Policy", "VIN received: 2HKRS4H70RH000123")
    index.search("priya vin")
    assert len(embedder.embedded) == first + 1
    assert "2HKRS4H70RH000123" in embedder.embedded[-1]


def test_warm_up_embeds_every_agent(workspace, embedder):
    _broker_roster(workspace)
    AgentIndex(workspace.roster, workspace.logs, embedder).warm_up()
    assert len(embedder.embedded) == 10


def test_search_during_warm_up_uses_keywords_instead_of_waiting(workspace, embedder):
    _broker_roster(workspace)
    index = AgentIndex(workspace.roster, workspace.logs, embedder)
    index._lock.acquire()  # as if the startup warm-up were still embedding
    try:
        started = time.perf_counter()
        cards = index.search("did priya send the VIN yet?", k=1)
        assert time.perf_counter() - started < 1.0
        assert agents(cards) == ["Priya Sharma Auto Policy"]
        assert embedder.embedded == []
    finally:
        index._lock.release()


def test_falls_back_to_keywords_when_embeddings_fail(workspace):
    class BrokenEmbedder:
        def passages(self, texts):
            raise RuntimeError("model download failed")

    _broker_roster(workspace)
    index = AgentIndex(workspace.roster, workspace.logs, BrokenEmbedder())
    assert agents(index.search("maya certificate", k=1)) == ["Certificate for Maya Cardenas"]
    assert index._embedder is None  # later searches skip embeddings


def test_empty_roster_and_empty_query(workspace, embedder):
    index = AgentIndex(workspace.roster, workspace.logs, embedder)
    assert index.search("anything") == []
    workspace.add("Lunch", entries_for("book lunch"))
    assert index.search("   ") == []
