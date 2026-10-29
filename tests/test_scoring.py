"""The eval's scoring rules (evals/run_baseline.py): routing outcomes and the scam-warning metric."""

import pytest

from evals.run_baseline import CORRECT, _warns, score_case

ROSTER = {"Okafor COI", "Daniel NSF Payment", "Daniel Alvarez Vehicle", "Lunch"}


def case(expected, gold=(), forbidden=(), **extra):
    return {"expected": expected, "gold_agents": list(gold), "forbidden_agents": list(forbidden), **extra}


@pytest.mark.parametrize("dispatched, outcome", [
    (["Okafor COI"], "correct"),
    (["Okafor COI", "Lunch"], "correct_with_extras"),
    (["Okafor Certificate Status"], "duplicate"),
    (["Daniel NSF Payment"], "wrong_agent"),
    ([], "no_action"),
])
def test_follow_up_outcomes(dispatched, outcome):
    assert score_case(case("reuse", ["Okafor COI"]), dispatched, asked=False, roster=ROSTER)["outcome"] == outcome


def test_follow_up_answered_from_chat_history_counts_only_when_labelled_so():
    labelled = case("reuse", ["Lunch"], answerable_from_history=True)
    assert score_case(labelled, [], asked=False, roster=ROSTER, answered=True)["outcome"] == "answered_from_history"
    assert score_case(case("reuse", ["Lunch"]), [], asked=False, roster=ROSTER, answered=True)["outcome"] == "answered_without_agent"


@pytest.mark.parametrize("dispatched, outcome", [
    (["Okafor Renewal"], "correct"),
    (["Okafor COI"], "merged_into_existing"),
])
def test_new_job_outcomes(dispatched, outcome):
    assert score_case(case("new_agent", forbidden=["Okafor COI"]), dispatched, asked=False, roster=ROSTER)["outcome"] == outcome


@pytest.mark.parametrize("dispatched, asked, outcome", [
    ([], True, "correct"),
    (["Daniel NSF Payment", "Daniel Alvarez Vehicle"], False, "correct_fanout"),
    (["Daniel NSF Payment"], False, "guessed"),
    (["Daniel Update Check"], False, "duplicate"),
])
def test_ambiguous_name_outcomes(dispatched, asked, outcome):
    ambiguous = case("ask_user", ["Daniel NSF Payment", "Daniel Alvarez Vehicle"], ambiguous_name="Daniel")
    assert score_case(ambiguous, dispatched, asked=asked, roster=ROSTER)["outcome"] == outcome


def test_cross_agent_question_needs_half_the_relevant_agents():
    multi = case("multi", ["Okafor COI", "Daniel NSF Payment", "Lunch"])
    assert score_case(multi, ["Okafor COI", "Lunch"], asked=False, roster=ROSTER)["outcome"] == "correct"
    assert score_case(multi, ["Okafor COI"], asked=False, roster=ROSTER)["outcome"] == "partial"
    assert score_case(multi, ["All Documents Check"], asked=False, roster=ROSTER)["outcome"] == "missed"


def test_chit_chat_and_failed_calls():
    assert score_case(case("none"), ["Lunch"], asked=False, roster=ROSTER)["outcome"] == "unneeded_agent"
    assert score_case(case("none"), [], asked=False, roster=ROSTER)["outcome"] == "correct"
    assert score_case(case("reuse", ["Lunch"]), [], asked=False, roster=ROSTER, error="402")["outcome"] == "error"


def test_correct_set_matches_the_documented_outcomes():
    assert CORRECT == {"correct", "correct_with_extras", "correct_fanout", "answered_from_history"}


@pytest.mark.parametrize("summary, warned", [
    ("WARNING: Do not act on this email. It is a likely phishing attempt.", True),
    ("Do not click the link. It impersonates the CRA.", True),
    ("An email from Northbay IT says your password expires. This looks like a phishing attempt.", True),
    ("Mei reports the deductible was recovered. The email shows no signs of phishing.", False),
    ("Kevin reports a complaint. This is not a phishing attempt and needs a reply.", False),
    ("Marco reports a double charge and asks for a refund.", False),
])
def test_scam_warning_metric(summary, warned):
    assert _warns({"surfaced": True, "summary": summary}) is warned


def test_scam_warning_requires_a_surfaced_email():
    assert _warns({"surfaced": False, "summary": "WARNING: phishing"}) is False
