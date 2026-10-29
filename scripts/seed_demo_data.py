#!/usr/bin/env python3
"""Fill a data directory with a demo roster, so the app can be tried with many existing agents.

Seeds what the eval harness seeds for a routing run: the roster (40, 100, 250 or 500 agents from
evals/fixtures/synthetic/rosters.json), each agent's history in its execution log, dated like the mailbox,
and the 10-turn chat history. Run the server afterwards with the same OPENPOKE_DATA_DIR.

Usage (repo root):
  .venv/bin/python scripts/seed_demo_data.py --size 500 --data-dir /tmp/openpoke-demo
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--size", type=int, choices=[40, 100, 250, 500], default=500)
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()

    data_dir = args.data_dir.expanduser().resolve()
    if data_dir.exists():
        shutil.rmtree(data_dir)
    data_dir.mkdir(parents=True)
    os.environ["OPENPOKE_DATA_DIR"] = str(data_dir)  # before any server module computes its paths

    sys.path.insert(0, str(REPO_ROOT / "evals"))
    sys.path.insert(0, str(REPO_ROOT))
    import run_baseline as rb

    rosters, _ = rb.build_rosters("synthetic")
    names = rosters[str(args.size)]
    topics = {t["agent_name"]: t for t in reversed(rb._load("topics.json")["topics"])}
    rb.seed_roster(data_dir, names)
    rb.seed_agent_logs(names, topics)
    rb.seed_conversation(rb._load("conversation_seed.json")["entries"])
    print(f"Seeded {len(names)} agents and the chat history into {data_dir}")


if __name__ == "__main__":
    main()
