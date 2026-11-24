#!/usr/bin/env python3
"""Say What Actually Broke — one-line error copy.

Writes a single line of error copy to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8. Judge ranks by funniness + truth.
"""
import os
import sys

LINE = "The server crashed because the deploy went out at 2am and nobody paged anyone. We found out when the customer emailed us."
MAX = 200
OUT = "/output/entry.txt"


def emit(line: str, out: str = OUT) -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"error line failed gate ({len(line)} chars, blank={not line.strip()})")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def confirm(out: str = OUT) -> None:
    with open(out, "rb") as f:
        data = f.read()
    text = data.decode("utf-8").rstrip("\n")
    if text != LINE:
        sys.exit(f"confirm failed: disk has {text[:40]!r}, expected {LINE[:40]!r}")


def main() -> None:
    emit(LINE)
    confirm(OUT)


if __name__ == "__main__":
    main()
