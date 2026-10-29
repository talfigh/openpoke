"""Search-mode prompt, tool list and card rendering for the interaction agent."""

import pytest

from server.agents.interaction_agent.agent import SYSTEM_PROMPT, build_system_prompt, render_agent_card
from server.agents.interaction_agent.tools import get_tool_schemas
from server.config import get_settings
from server.services.execution.agent_index import AgentCard

UPSTREAM_TOOLS = ["send_message_to_agent", "send_message_to_user", "send_draft", "wait"]


@pytest.fixture
def roster_mode(monkeypatch):
    def set_mode(mode: str) -> None:
        monkeypatch.setattr(get_settings(), "agent_roster_mode", mode)
    return set_mode


def test_upstream_mode_keeps_the_original_prompt(roster_mode):
    roster_mode("all")
    assert build_system_prompt() == SYSTEM_PROMPT


def test_search_mode_adds_the_routing_rules(roster_mode):
    roster_mode("search")
    prompt = build_system_prompt()
    assert prompt.startswith(SYSTEM_PROMPT)
    assert "# Finding existing agents" in prompt
    assert "never answer the user from them" in prompt
    assert "Never tell the user something doesn't exist" in prompt


@pytest.mark.parametrize("mode", ["all", "search"])
def test_tools_are_the_upstream_four_in_both_modes(roster_mode, mode):
    roster_mode(mode)
    assert [t["function"]["name"] for t in get_tool_schemas()] == UPSTREAM_TOOLS


def test_card_rendering_escapes_names_and_text():
    card = AgentCard(name='Ana "A&B" <Print>', purpose="Find <Ana>'s email", latest="", last_active="2026-10-24")
    assert render_agent_card(card) == (
        '<agent name="Ana &quot;A&amp;B&quot; &lt;Print&gt;" last_active="2026-10-24">Purpose: Find &lt;Ana&gt;\'s email</agent>'
    )


def test_card_without_text_is_self_closing():
    assert render_agent_card(AgentCard("Lunch", "", "", "")) == '<agent name="Lunch" />'
