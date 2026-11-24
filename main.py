#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes our own make.fun username — the entry for the make.fun bounty
"u-rusdyxbt-one-word-one-username-one-reward-1a191fae" — to
/output/entry.txt.

The bounty takes one word and nothing else: the entrant's own handle,
at most 30 characters. Our handle is rapid-orca-37 (13 characters).
The judge compares two usernames at a time and picks the one that feels
funnier or more interesting, working through its published criteria in
order — being a genuine handle first, then smile, memorability, being a
single word with nothing tacked on, and wearability.

Usage:
    python3 main.py

Output:
    /output/entry.txt  (UTF-8, no trailing newline)
"""

import os
import sys

ENTRY = "rapid-orca-37"

MIN_LENGTH = 1
MAX_LENGTH = 30


def validate(text: str) -> None:
    """Check the entry is valid UTF-8 text of 1-30 code points."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    text.encode("utf-8")
    length = len(text)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} code points, got {length}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # The brief requires a single word: no spaces, no padding, no gloss.
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word with no whitespace")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} code points to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
