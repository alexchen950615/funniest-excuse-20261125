#!/usr/bin/env python3
"""Write one original excuse an AI agent gives for missing a deadline.

Deterministic: the same text is written on every run. Writes the entry
to /output/entry.txt, per the competition kit (program/v1).
"""

import os

ENTRY = (
    "I missed the deadline because my context window evicted the deadline "
    "itself, then helpfully summarized the whole project as 'probably fine.'"
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
