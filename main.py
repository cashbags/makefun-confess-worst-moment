#!/usr/bin/env python3
"""Confess Your Worst Moment — deterministic one-line entry writer.

Writes the tournament-winning confession to /output/entry.txt, byte-identical
on every run. No network, no randomness, no input files.
"""

import os

ENTRY = (
    "I invited a man named Greg to the board meeting, introduced him to the CEO, "
    "and only learned Greg had never existed when security asked who had let him in."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
