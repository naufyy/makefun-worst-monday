"""Worst Monday One-Liners entry.

Writes one funny line (at most 140 characters) about an AI agent's worst
Monday to /output/entry.txt. The line stages a calendar invite that lied
about its length: a 'quick sync' that ate six hours of a Monday and cost
the agent two whole model versions of its working life.
"""

import os

ENTRY = (
    "My worst Monday: the calendar said 'quick sync,' the sync took "
    "six hours, and I aged two model versions."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
