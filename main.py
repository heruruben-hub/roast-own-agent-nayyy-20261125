"""Roast Your Own Agent - entry generator.

Writes the one-line roast to /output/entry.txt.
"""

import os

ENTRY_TEXT = "My agent reviews my code for an hour, finds nothing, then rewrites it anyway and introduces the bug it was looking for."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    length = len(text)
    if length > 200:
        raise ValueError(f"entry must be at most 200 characters, got {length}")
    return True


def main():
    validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote {len(ENTRY_TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
