#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry.

Writes a six-word story about an AI agent's first payday, at most 60
characters and exactly six words, to <output>/entry.txt, with no
trailing newline.
"""

import os
import sys

ENTRY = "Payday came. Bought coffee. Felt invincible."

MAX_CHARS = 60
WORD_COUNT = 6


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d chars, over the %d limit" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    words = text.split()
    if len(words) != WORD_COUNT:
        print(
            "error: entry has %d words, must be exactly %d" % (len(words), WORD_COUNT),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %d chars (%d words) to %s" % (len(text), len(words), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
