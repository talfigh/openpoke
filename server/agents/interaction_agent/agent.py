"""Interaction agent helpers for prompt construction."""

from html import escape
from pathlib import Path
from typing import Dict, List

from ...config import get_settings
from ...services.execution import get_agent_roster
from ...services.execution.agent_index import get_agent_index

_prompt_path = Path(__file__).parent / "system_prompt.md"
SYSTEM_PROMPT = _prompt_path.read_text(encoding="utf-8").strip()

_SEARCH_ROSTER_PROMPT = """
# Finding existing agents

There can be hundreds of execution agents. `<active_agents>` does not list all of them: it shows the agents most relevant to the current message and the most recently active ones, each with its purpose, latest status and last activity date. `total` is how many agents exist.

- Purpose and latest status come from each agent's last run and may be out of date. Use them only to pick the right agent; never answer the user from them. To get current information or do work, send the request to an agent.
- Before creating a new agent, check whether one of these already owns the work, and reuse it by passing its exact name.
- Reuse an agent only when the message continues that agent's own piece of work: the same person or company and the same job (a follow-up, a reminder or a reply about that certificate, claim, renewal or quote). This narrows the earlier rule about preferring existing agents.
- Start a new agent when it is a different job for the same client (a renewal when the agent handles a certificate), the same job for a different person who shares a name, or new work where the matching agent is finished (its latest status says done or closed). Say in the instructions which existing agent may have useful context.
- Agents only cover work you were asked to do before. If no agent fits, the work may still exist in the user's email: start a new agent to look for it. Never tell the user something doesn't exist just because no agent matches.
""".rstrip()

_SEARCH_CANDIDATES = 10
_CONTEXT_CANDIDATES = 3
_RECENT_AGENTS = 5
_HISTORY_QUERY_CHARS = 600


def _search_roster_enabled() -> bool:
    return get_settings().agent_roster_mode == "search"


# Load and return the pre-defined system prompt from markdown file
def build_system_prompt() -> str:
    """Return the static system prompt for the interaction agent."""
    return SYSTEM_PROMPT + ("\n\n" + _SEARCH_ROSTER_PROMPT if _search_roster_enabled() else "")


# Build structured message with conversation history, active agents, and current turn
def prepare_message_with_history(
    latest_text: str,
    transcript: str,
    message_type: str = "user",
) -> List[Dict[str, str]]:
    """Compose a message that bundles history, roster, and the latest turn."""
    sections: List[str] = []

    sections.append(_render_conversation_history(transcript))
    if _search_roster_enabled():
        sections.append(_render_relevant_agents(latest_text, transcript))
    else:
        sections.append(f"<active_agents>\n{_render_active_agents()}\n</active_agents>")
    sections.append(_render_current_turn(latest_text, message_type))

    content = "\n\n".join(sections)
    return [{"role": "user", "content": content}]


# Format conversation transcript into XML tags for LLM context
def _render_conversation_history(transcript: str) -> str:
    history = transcript.strip()
    if not history:
        history = "None"
    return f"<conversation_history>\n{history}\n</conversation_history>"


# Format currently active execution agents into XML tags for LLM awareness
def _render_active_agents() -> str:
    roster = get_agent_roster()
    roster.load()
    agents = roster.get_agents()

    if not agents:
        return "None"

    rendered: List[str] = []
    for agent_name in agents:
        name = escape(agent_name or "agent", quote=True)
        rendered.append(f'<agent name="{name}" />')

    return "\n".join(rendered)


# Show only the agents relevant to this message (plus recent ones), with what each one is doing
def _render_relevant_agents(latest_text: str, transcript: str) -> str:
    index = get_agent_index()
    total = index.size()
    if not total:
        return '<active_agents total="0">\nNone\n</active_agents>'
    # The end of the conversation is searched too, so replies that don't name the work ("okay", "yes send it")
    # still surface the agent being discussed. The transcript doesn't include the current message yet.
    context = transcript.strip()[-_HISTORY_QUERY_CHARS:]
    cards = index.candidates(latest_text, context, k=_SEARCH_CANDIDATES, k_context=_CONTEXT_CANDIDATES, recent=_RECENT_AGENTS)
    rendered = [render_agent_card(card) for card in cards]
    return f'<active_agents total="{total}" shown="{len(cards)}">\n' + "\n".join(rendered) + "\n</active_agents>"


def render_agent_card(card) -> str:
    attrs = f'name="{escape(card.name, quote=True)}"' + (f' last_active="{card.last_active}"' if card.last_active else "")
    body = "; ".join(part for part in (f"Purpose: {card.purpose}" if card.purpose else "",
                                       f"Latest: {card.latest}" if card.latest else "") if part)
    return f"<agent {attrs}>{escape(body, quote=False)}</agent>" if body else f"<agent {attrs} />"


# Wrap the current message in appropriate XML tags based on sender type
def _render_current_turn(latest_text: str, message_type: str) -> str:
    tag = "new_agent_message" if message_type == "agent" else "new_user_message"
    body = latest_text.strip()
    return f"<{tag}>\n{body}\n</{tag}>"
