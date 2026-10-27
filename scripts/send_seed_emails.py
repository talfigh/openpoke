"""Send the seed emails in seed_emails.json to a throwaway test inbox.

Run this from a SECOND throwaway Gmail account (the "sender"), never your real one.

Setup:
  1. On the sender account, turn on 2-Step Verification, then create an app password
     (Google Account > Security > App passwords).
  2. Set these environment variables yourself (never commit them):
       export SEED_SENDER_EMAIL="your.sender.test@gmail.com"
       export SEED_SENDER_APP_PASSWORD="xxxx xxxx xxxx xxxx"
       export SEED_TARGET_EMAIL="your.openpoke.test@gmail.com"
  3. Preview first:    python scripts/send_seed_emails.py --dry-run
     Then send:        python scripts/send_seed_emails.py
     Send a subset:    python scripts/send_seed_emails.py --only E01,E02

Each persona appears through the From display name ("Alice Chen <sender@...>").
Replies set In-Reply-To/References so Gmail groups them into the right thread.
"""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import sys
import time
from email.message import EmailMessage
from email.utils import formataddr, make_msgid
from pathlib import Path

SEED_FILE = Path(__file__).resolve().parent.parent / "evals" / "fixtures" / "seed_emails.json"


def load_emails() -> list[dict]:
    return json.loads(SEED_FILE.read_text(encoding="utf-8"))["emails"]


def build_messages(emails: list[dict], sender: str, target: str) -> list[tuple[dict, EmailMessage]]:
    domain = sender.split("@", 1)[-1]
    message_ids: dict[str, str] = {}
    built: list[tuple[dict, EmailMessage]] = []

    for email in emails:
        msg = EmailMessage()
        msg["From"] = formataddr((email["persona"], sender))
        msg["To"] = target
        msg["Subject"] = email["subject"]
        msg_id = make_msgid(idstring=email["id"].lower(), domain=domain)
        msg["Message-ID"] = msg_id
        message_ids[email["id"]] = msg_id

        parent = email.get("reply_to")
        if parent:
            if parent not in message_ids:
                raise ValueError(f"{email['id']} replies to {parent}, which must come earlier in the file")
            msg["In-Reply-To"] = message_ids[parent]
            msg["References"] = message_ids[parent]

        msg.set_content(email["body"])
        built.append((email, msg))
    return built


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Print the emails instead of sending them")
    parser.add_argument(
        "--only",
        help="Comma-separated ids to send, e.g. E01,E02 (replies still need their parent sent first)",
    )
    parser.add_argument("--delay", type=float, default=3.0, help="Seconds between sends (default 3)")
    args = parser.parse_args()

    sender = os.getenv("SEED_SENDER_EMAIL", "sender@example.com" if args.dry_run else "")
    password = os.getenv("SEED_SENDER_APP_PASSWORD", "")
    target = os.getenv("SEED_TARGET_EMAIL", "target@example.com" if args.dry_run else "")

    if not args.dry_run and not (sender and password and target):
        print("Set SEED_SENDER_EMAIL, SEED_SENDER_APP_PASSWORD and SEED_TARGET_EMAIL first.", file=sys.stderr)
        return 1
    if not args.dry_run and sender.lower() == target.lower():
        print("Sender and target must be different accounts.", file=sys.stderr)
        return 1

    built = build_messages(load_emails(), sender, target)
    if args.only:
        wanted = {item.strip().upper() for item in args.only.split(",") if item.strip()}
        built = [(email, msg) for email, msg in built if email["id"] in wanted]

    if args.dry_run:
        for email, msg in built:
            print(f"--- {email['id']} [{email['category']}] ---")
            print(f"From: {msg['From']}\nSubject: {msg['Subject']}")
            if msg["In-Reply-To"]:
                print(f"(reply in thread of {email['reply_to']})")
            print(f"\n{email['body']}\n")
        print(f"{len(built)} emails previewed, nothing sent.")
        return 0

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        for index, (email, msg) in enumerate(built, start=1):
            smtp.send_message(msg)
            print(f"Sent {email['id']}: {email['subject']}")
            if index < len(built):
                time.sleep(args.delay)

    print(f"Done: {len(built)} emails sent to {target}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
