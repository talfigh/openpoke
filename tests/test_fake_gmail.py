"""Gmail query matching in the fake backend (server/services/gmail/fake_backend.py)."""

from datetime import datetime, timezone

import pytest

from server.services.gmail.fake_backend import compile_query

NOW = datetime(2026, 10, 27, 17, 0, tzinfo=timezone.utc)
MSG = {
    "subject": "Re: Certificate of insurance needed for city contract",
    "sender": "Daniel Okafor <daniel@okaforlandscaping.example>",
    "to": "sam.rivera@northbaybrokers.example",
    "messageText": "The holder must read The Corporation of the City of Vaughan. Province of Ontario.",
    "labelIds": ["INBOX", "IMPORTANT"],
    "messageTimestamp": "2026-10-25T14:00:00Z",
    "attachmentList": [{"filename": "contract.pdf"}],
}


@pytest.mark.parametrize("query, matches", [
    ("vaughan", True),
    ("vin", False),  # whole words only: "vin" must not match "province"
    ('"city of vaughan"', True),
    ("from:okafor", True),
    ("from:priya", False),
    ("subject:certificate -subject:newsletter", True),
    ("subject:renewal OR subject:certificate", True),
    ("label:IMPORTANT has:attachment filename:pdf", True),
    ("newer_than:7d", True),
    ("older_than:7d", False),
])
def test_query_matching(query, matches):
    assert compile_query(query, NOW)(dict(MSG)) is matches
