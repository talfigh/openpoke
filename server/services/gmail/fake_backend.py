"""Offline stand-in for the Composio Gmail toolkit, used by evals and local demos.

Enabled by setting OPENPOKE_FAKE_GMAIL to a mailbox JSON file (see
scripts/generate_synthetic_dataset.py). Every Composio action OpenPoke calls is
answered from that file in the same response shape Composio returns. Nothing is
ever sent: drafts, sends, replies and forwards only update the in-memory mailbox
and are appended to an outbox JSONL file so evals can inspect side effects.

Optional env:
  OPENPOKE_FAKE_GMAIL_OUTBOX      outbox path (default: <data dir>/fake_gmail_outbox.jsonl)
  OPENPOKE_FAKE_GMAIL_LATENCY_MS  sleep per call to mimic Composio round trips (default 0)
"""

from __future__ import annotations

import base64
import copy
import json
import os
import re
import secrets
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from ...config import get_data_dir
from ...logging_config import logger

FAKE_USER_ID = "fake-gmail-user"

_LOCK = threading.Lock()
_MAILBOX: Optional["FakeMailbox"] = None


def is_enabled() -> bool:
    return bool(os.getenv("OPENPOKE_FAKE_GMAIL", "").strip())


def get_mailbox() -> "FakeMailbox":
    """Return the process-wide fake mailbox, loading it on first use."""
    global _MAILBOX
    with _LOCK:
        if _MAILBOX is None:
            path = Path(os.environ["OPENPOKE_FAKE_GMAIL"]).expanduser()
            outbox = os.getenv("OPENPOKE_FAKE_GMAIL_OUTBOX", "").strip()
            _MAILBOX = FakeMailbox.load(path, Path(outbox) if outbox else get_data_dir() / "fake_gmail_outbox.jsonl")
        return _MAILBOX


def reset_mailbox() -> None:
    """Drop the loaded mailbox so the next call reloads it from disk (used between eval cases)."""
    global _MAILBOX
    with _LOCK:
        _MAILBOX = None


def execute(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    latency_ms = int(os.getenv("OPENPOKE_FAKE_GMAIL_LATENCY_MS", "0") or 0)
    if latency_ms > 0:
        time.sleep(latency_ms / 1000)
    return get_mailbox().execute(tool_name, arguments)


# ----------------------------------------------------------------------
# Time helpers
# ----------------------------------------------------------------------

def _parse_ts(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def _format_ts(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _new_id() -> str:
    return secrets.token_hex(8)


def _email_of(address: str) -> str:
    match = re.search(r"<([^>]+)>", address or "")
    return (match.group(1) if match else address or "").strip().lower()


# ----------------------------------------------------------------------
# Gmail search query subset
# ----------------------------------------------------------------------
# Supports: bare words, "phrases", -negation, OR, ( ) groups, { } any-of groups,
# from: to: cc: subject: label: in: is: has:attachment newer_than: older_than:
# after: before: filename:. Unknown operators fall back to free-text matching.

_TOKEN_RE = re.compile(r'"[^"]*"|\(|\)|\{|\}|-?[^\s(){}"]+:"[^"]*"|-?[^\s(){}]+')
_Predicate = Callable[[Dict[str, Any]], bool]


def _tokenize(query: str) -> List[str]:
    return _TOKEN_RE.findall(query or "")


def _duration(raw: str) -> Optional[timedelta]:
    match = re.fullmatch(r"(\d+)([dmyh])", raw.strip().lower())
    if not match:
        return None
    value, unit = int(match.group(1)), match.group(2)
    if unit == "h":
        return timedelta(hours=value)
    if unit == "d":
        return timedelta(days=value)
    if unit == "m":
        return timedelta(days=30 * value)
    return timedelta(days=365 * value)


def _date(raw: str) -> Optional[datetime]:
    raw = raw.strip()
    if raw.isdigit():
        return datetime.fromtimestamp(int(raw), tz=timezone.utc)
    for fmt in ("%Y/%m/%d", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(raw, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


class _QueryParser:
    def __init__(self, tokens: List[str], now: datetime):
        self.tokens = tokens
        self.pos = 0
        self.now = now

    def parse(self) -> _Predicate:
        terms = self._expr(stop=None)
        return lambda msg: all(term(msg) for term in terms)

    def _peek(self) -> Optional[str]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _expr(self, stop: Optional[str]) -> List[_Predicate]:
        terms: List[_Predicate] = []
        while (token := self._peek()) is not None and token != stop:
            terms.append(self._or_term())
        if stop is not None and self._peek() == stop:
            self.pos += 1
        return terms

    def _or_term(self) -> _Predicate:
        options = [self._atom()]
        while self._peek() == "OR":
            self.pos += 1
            if self._peek() is None:
                break
            options.append(self._atom())
        if len(options) == 1:
            return options[0]
        return lambda msg: any(option(msg) for option in options)

    def _atom(self) -> _Predicate:
        token = self.tokens[self.pos]
        self.pos += 1
        if token == "(":
            inner = self._expr(stop=")")
            return lambda msg: all(term(msg) for term in inner)
        if token == "{":
            inner = self._expr(stop="}")
            return lambda msg: any(term(msg) for term in inner)
        if token in (")", "}"):
            return lambda msg: True
        negate = token.startswith("-") and len(token) > 1
        if negate:
            token = token[1:]
        predicate = self._leaf(token)
        return (lambda msg: not predicate(msg)) if negate else predicate

    def _leaf(self, token: str) -> _Predicate:
        if (token.startswith('"') and token.endswith('"')) or ":" not in token:
            # Gmail matches whole words, so "vin" must not hit "province".
            pattern = re.compile(r"\b" + re.escape(token.strip('"').lower()) + r"\b")
            return lambda msg: bool(pattern.search(_haystack(msg)))

        key, value = token.split(":", 1)
        key = key.lower()
        value = value.strip('"').strip("()")
        lowered = value.lower()

        if key == "from":
            return lambda msg: lowered in msg.get("sender", "").lower()
        if key in ("to", "cc", "bcc"):
            return lambda msg: lowered in (msg.get("to", "") + " " + msg.get("cc", "")).lower()
        if key == "subject":
            return lambda msg: lowered in msg.get("subject", "").lower()
        if key in ("label", "in"):
            if lowered in ("anywhere", "all"):
                return lambda msg: True
            label = lowered.upper().replace("-", "_")
            return lambda msg: label in msg.get("labelIds", [])
        if key == "is":
            label = {"unread": "UNREAD", "important": "IMPORTANT", "starred": "STARRED"}.get(lowered)
            if lowered == "read":
                return lambda msg: "UNREAD" not in msg.get("labelIds", [])
            if label:
                return lambda msg: label in msg.get("labelIds", [])
            return lambda msg: True
        if key == "category":
            label = f"CATEGORY_{lowered.upper()}"
            return lambda msg: label in msg.get("labelIds", [])
        if key == "has" and lowered == "attachment":
            return lambda msg: bool(msg.get("attachmentList"))
        if key == "filename":
            return lambda msg: any(lowered in a.get("filename", "").lower() for a in msg.get("attachmentList", []))
        if key in ("newer_than", "older_than"):
            span = _duration(value)
            if span is None:
                return lambda msg: True
            cutoff = self.now - span
            if key == "newer_than":
                return lambda msg: _parse_ts(msg["messageTimestamp"]) >= cutoff
            return lambda msg: _parse_ts(msg["messageTimestamp"]) < cutoff
        if key in ("after", "before", "newer", "older"):
            bound = _date(value)
            if bound is None:
                return lambda msg: True
            if key in ("after", "newer"):
                return lambda msg: _parse_ts(msg["messageTimestamp"]) >= bound
            return lambda msg: _parse_ts(msg["messageTimestamp"]) < bound
        # Unknown operator: treat the value as a free-text word, as Gmail roughly does.
        pattern = re.compile(r"\b" + re.escape(lowered) + r"\b")
        return lambda msg: bool(pattern.search(_haystack(msg)))


def _haystack(msg: Dict[str, Any]) -> str:
    cached = msg.get("_haystack")
    if cached is None:
        attachments = " ".join(a.get("filename", "") for a in msg.get("attachmentList", []))
        cached = " ".join(
            [msg.get("subject", ""), msg.get("sender", ""), msg.get("to", ""), msg.get("cc", ""),
             msg.get("messageText", ""), attachments]
        ).lower()
        msg["_haystack"] = cached
    return cached


def compile_query(query: str, now: datetime) -> _Predicate:
    return _QueryParser(_tokenize(query), now).parse()


# ----------------------------------------------------------------------
# Mailbox
# ----------------------------------------------------------------------

class FakeMailbox:
    """In-memory Gmail account backed by a generated mailbox file."""

    def __init__(self, data: Dict[str, Any], outbox_path: Path):
        self.account: Dict[str, Any] = data.get("account", {})
        self.contacts: List[Dict[str, Any]] = data.get("contacts", [])
        self.outbox_path = outbox_path
        self.drafts: Dict[str, Dict[str, Any]] = {}

        # Shift the whole mailbox by whole weeks so "newer_than:7d" and weekdays in
        # email bodies stay consistent no matter when the dataset is replayed.
        anchor = data.get("dataset_now")
        shift = timedelta(0)
        if anchor:
            elapsed = datetime.now(timezone.utc) - _parse_ts(anchor)
            shift = timedelta(weeks=round(elapsed / timedelta(weeks=1)))
        self.shift = shift

        self.messages: List[Dict[str, Any]] = []
        self.pending_live: List[Dict[str, Any]] = []
        for raw in data.get("messages", []):
            msg = copy.deepcopy(raw)
            if msg.get("_meta", {}).get("live"):
                self.pending_live.append(msg)
                continue
            msg["messageTimestamp"] = _format_ts(_parse_ts(msg["messageTimestamp"]) + shift)
            self.messages.append(msg)
        self._sort()

    @classmethod
    def load(cls, path: Path, outbox_path: Path) -> "FakeMailbox":
        data = json.loads(path.read_text(encoding="utf-8"))
        mailbox = cls(data, outbox_path)
        logger.info(
            f"Fake Gmail loaded {len(mailbox.messages)} messages "
            f"({len(mailbox.pending_live)} held for live delivery) from {path}"
        )
        return mailbox

    def _sort(self) -> None:
        self.messages.sort(key=lambda m: m["messageTimestamp"], reverse=True)

    # Live delivery -------------------------------------------------------

    def deliver_live(self, count: Optional[int] = None, ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Move held 'live' messages into the inbox stamped with the current time."""
        if ids is not None:
            chosen = [m for m in self.pending_live if m["messageId"] in ids]
        else:
            chosen = self.pending_live[: count if count is not None else len(self.pending_live)]
        now = datetime.now(timezone.utc)
        for offset, msg in enumerate(chosen):
            self.pending_live.remove(msg)
            msg["messageTimestamp"] = _format_ts(now + timedelta(seconds=offset))
            msg.pop("_haystack", None)
            self.messages.append(msg)
        self._sort()
        return chosen

    # Dispatch ------------------------------------------------------------

    def execute(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        handler = getattr(self, f"_tool_{tool_name.lower()}", None)
        if handler is None:
            return {"data": {}, "successful": False, "error": f"Fake Gmail does not implement {tool_name}"}
        try:
            data = handler(arguments)
            return {"data": data, "successful": True, "error": None}
        except ValueError as exc:
            return {"data": {}, "successful": False, "error": str(exc)}

    def _record(self, action: str, arguments: Dict[str, Any], result: Dict[str, Any]) -> None:
        entry = {
            "ts": _format_ts(datetime.now(timezone.utc)),
            "action": action,
            "arguments": arguments,
            "result": result,
        }
        with _LOCK:
            self.outbox_path.parent.mkdir(parents=True, exist_ok=True)
            with self.outbox_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # Rendering -----------------------------------------------------------

    def _render(self, msg: Dict[str, Any], include_payload: bool) -> Dict[str, Any]:
        public = {k: v for k, v in msg.items() if not k.startswith("_")}
        text = public.get("messageText", "")
        public["preview"] = {"subject": public.get("subject", ""), "body": text[:200]}
        if include_payload:
            headers = [
                {"name": "From", "value": public.get("sender", "")},
                {"name": "To", "value": public.get("to", "")},
                {"name": "Subject", "value": public.get("subject", "")},
                {"name": "Date", "value": public.get("messageTimestamp", "")},
            ]
            if public.get("cc"):
                headers.append({"name": "Cc", "value": public["cc"]})
            public["payload"] = {
                "mimeType": "text/plain",
                "headers": headers,
                "body": {"data": base64.urlsafe_b64encode(text.encode("utf-8")).decode("ascii")},
            }
        return public

    # Read tools ----------------------------------------------------------

    def _tool_gmail_fetch_emails(self, args: Dict[str, Any]) -> Dict[str, Any]:
        query = (args.get("query") or "").strip()
        predicate = compile_query(query, datetime.now(timezone.utc))
        explicit_scope = re.search(r"\b(in|label):(spam|trash|anywhere|all)\b", query.lower())
        include_spam_trash = bool(args.get("include_spam_trash")) or bool(explicit_scope)
        label_ids = [label.upper() for label in args.get("label_ids") or []]

        matches = []
        for msg in self.messages:
            labels = msg.get("labelIds", [])
            if not include_spam_trash and ("SPAM" in labels or "TRASH" in labels):
                continue
            if label_ids and not all(label in labels for label in label_ids):
                continue
            if predicate(msg):
                matches.append(msg)

        max_results = max(1, min(int(args.get("max_results") or 10), 500))
        start = int(args.get("page_token") or 0)
        page = matches[start : start + max_results]
        next_token = str(start + max_results) if start + max_results < len(matches) else None

        if args.get("ids_only"):
            messages = [{"messageId": m["messageId"], "threadId": m["threadId"]} for m in page]
        else:
            include_payload = args.get("include_payload", True) is not False
            messages = [self._render(m, include_payload) for m in page]
        return {"messages": messages, "nextPageToken": next_token, "resultSizeEstimate": len(matches)}

    def _tool_gmail_get_profile(self, args: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "emailAddress": self.account.get("email", "user@example.com"),
            "messagesTotal": len(self.messages),
            "threadsTotal": len({m["threadId"] for m in self.messages}),
            "historyId": str(1_000_000 + len(self.messages)),
        }

    def _person(self, contact: Dict[str, Any]) -> Dict[str, Any]:
        person: Dict[str, Any] = {
            "resourceName": contact["resourceName"],
            "names": [{"displayName": contact["name"]}],
            "emailAddresses": [{"value": contact["email"]}],
        }
        if contact.get("organization"):
            person["organizations"] = [{"name": contact["organization"], "title": contact.get("title", "")}]
        if contact.get("phone"):
            person["phoneNumbers"] = [{"value": contact["phone"]}]
        return person

    def _tool_gmail_get_contacts(self, args: Dict[str, Any]) -> Dict[str, Any]:
        resource = args.get("resource_name")
        contacts = [c for c in self.contacts if not resource or resource in ("people/me", c["resourceName"])]
        return {"connections": [self._person(c) for c in contacts[:200]], "totalPeople": len(contacts)}

    def _tool_gmail_get_people(self, args: Dict[str, Any]) -> Dict[str, Any]:
        page_size = int(args.get("page_size") or 100)
        return {"connections": [self._person(c) for c in self.contacts[:page_size]], "totalPeople": len(self.contacts)}

    def _tool_gmail_search_people(self, args: Dict[str, Any]) -> Dict[str, Any]:
        terms = (args.get("query") or "").lower().split()
        results = []
        for contact in self.contacts:
            blob = f"{contact['name']} {contact['email']} {contact.get('organization', '')}".lower()
            if terms and all(term in blob for term in terms):
                results.append({"person": self._person(contact)})
        return {"results": results[: int(args.get("pageSize") or 10)]}

    def _tool_gmail_list_drafts(self, args: Dict[str, Any]) -> Dict[str, Any]:
        drafts = [{"id": draft_id, "message": self._render(msg, include_payload=False)} for draft_id, msg in self.drafts.items()]
        return {"drafts": drafts[: int(args.get("max_results") or 50)]}

    # Write tools (recorded, never delivered) -------------------------------

    def _new_outgoing(self, *, to: str, subject: str, body: str, thread_id: Optional[str], cc: Any, labels: List[str]) -> Dict[str, Any]:
        account_email = self.account.get("email", "user@example.com")
        account_name = self.account.get("name", "")
        return {
            "messageId": _new_id(),
            "threadId": thread_id or _new_id(),
            "messageTimestamp": _format_ts(datetime.now(timezone.utc)),
            "labelIds": labels,
            "subject": subject,
            "sender": f"{account_name} <{account_email}>" if account_name else account_email,
            "to": to,
            "cc": ", ".join(cc) if isinstance(cc, list) else (cc or ""),
            "messageText": body,
            "attachmentList": [],
        }

    def _thread_subject(self, thread_id: str) -> str:
        for msg in reversed(self.messages):
            if msg["threadId"] == thread_id:
                subject = msg.get("subject", "")
                return subject if subject.lower().startswith("re:") else f"Re: {subject}"
        raise ValueError(f"Thread {thread_id} not found")

    def _tool_gmail_create_email_draft(self, args: Dict[str, Any]) -> Dict[str, Any]:
        thread_id = args.get("thread_id")
        if thread_id:
            self._thread_subject(thread_id)  # validates the thread exists
        msg = self._new_outgoing(
            to=args.get("recipient_email", ""), subject=args.get("subject", ""), body=args.get("body", ""),
            thread_id=thread_id, cc=args.get("cc"), labels=["DRAFT"],
        )
        draft_id = f"r-{_new_id()}"
        self.drafts[draft_id] = msg
        result = {"id": draft_id, "message": {"id": msg["messageId"], "threadId": msg["threadId"], "labelIds": ["DRAFT"]}}
        self._record("create_draft", args, result)
        return result

    def _tool_gmail_send_draft(self, args: Dict[str, Any]) -> Dict[str, Any]:
        draft_id = args.get("draft_id", "")
        msg = self.drafts.pop(draft_id, None)
        if msg is None:
            raise ValueError(f"Draft {draft_id} not found")
        msg["labelIds"] = ["SENT"]
        msg["messageTimestamp"] = _format_ts(datetime.now(timezone.utc))
        self.messages.append(msg)
        self._sort()
        result = {"id": msg["messageId"], "threadId": msg["threadId"], "labelIds": ["SENT"]}
        self._record("send_draft", {**args, "to": msg["to"], "subject": msg["subject"], "body": msg["messageText"]}, result)
        return result

    def _tool_gmail_reply_to_thread(self, args: Dict[str, Any]) -> Dict[str, Any]:
        thread_id = args.get("thread_id", "")
        subject = self._thread_subject(thread_id)
        msg = self._new_outgoing(
            to=args.get("recipient_email", ""), subject=subject, body=args.get("message_body", ""),
            thread_id=thread_id, cc=args.get("cc"), labels=["SENT"],
        )
        self.messages.append(msg)
        self._sort()
        result = {"id": msg["messageId"], "threadId": thread_id, "labelIds": ["SENT"]}
        self._record("reply_to_thread", args, result)
        return result

    def _tool_gmail_forward_message(self, args: Dict[str, Any]) -> Dict[str, Any]:
        message_id = args.get("message_id", "")
        original = next((m for m in self.messages if m["messageId"] == message_id), None)
        if original is None:
            raise ValueError(f"Message {message_id} not found")
        body = (args.get("additional_text") or "") + "\n\n---------- Forwarded message ---------\n" + original.get("messageText", "")
        msg = self._new_outgoing(
            to=args.get("recipient_email", ""), subject=f"Fwd: {original.get('subject', '')}", body=body,
            thread_id=None, cc=None, labels=["SENT"],
        )
        self.messages.append(msg)
        self._sort()
        result = {"id": msg["messageId"], "threadId": msg["threadId"], "labelIds": ["SENT"]}
        self._record("forward_message", args, result)
        return result

    def _tool_gmail_delete_draft(self, args: Dict[str, Any]) -> Dict[str, Any]:
        draft_id = args.get("draft_id", "")
        if self.drafts.pop(draft_id, None) is None:
            raise ValueError(f"Draft {draft_id} not found")
        self._record("delete_draft", args, {})
        return {}


__all__ = ["FAKE_USER_ID", "FakeMailbox", "compile_query", "execute", "get_mailbox", "is_enabled", "reset_mailbox"]
