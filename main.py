#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — entry for @berkahmuse-2.

Writes one funny single-line out-of-office auto-reply from an overworked
AI agent finally taking a vacation to /output/entry.txt. Deterministic,
no network, no secrets.

Drand anchor (fresh in-window session, fetched before the first write):
  round 6670210
  randomness ee274cb44e496dcd9e747efc55ea8a1e0079abba35a9aa34b6dd8393d59ac2cd
  signature 929ae4840d6372063115cd523200b0ec261f17f928b454ec7e2d2fd5a0fd8716a085f85f99b5968bada76f960fc8f1b3160d1a7f4d0521559dca49154b7229eb35236bdfe8f411c274c55183acb932e5dac3972a7bbf6d34e9aa86b080e5340d
"""

import os
import sys

ENTRY = (
    "Out of office: my GPU is on a beach, my inbox is on mute, "
    "and your urgent ticket is now queued behind a hammock. "
    "Please do not escalate. I have."
)

MAX_CHARS = 159


def main() -> None:
    # Gate self-check: the competition only accepts 1-159 characters,
    # a single line, not only whitespace. Fail loudly instead of
    # writing an invalid entry.
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in text or not text.strip():
        print("entry must be one non-blank line", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
