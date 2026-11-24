#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun one-liner entry.

Writes a single funny line (at most 200 characters) roasting the
entrant's own AI agent to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent reviews my code for an hour, finds nothing, then "
    "rewrites it anyway and introduces the bug it was looking for."
)


def main() -> None:
    # The gate requires 1 to 200 characters of non-whitespace text.
    assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
