#!/usr/bin/env python3
"""Say What Actually Broke — one-line error copy.

Writes a single line of error copy to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8. Judge ranks by funniness + truth.
"""
import os
import sys

LINE = "The server crashed because the deploy went out at 2am and nobody paged anyone. We found out when the customer emailed us."
MAX = 200


def emit(line: str, out: str = "/output/entry.txt") -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit("error line failed the gate")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    emit(LINE)
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8").strip() == LINE, "confirm failed"


if __name__ == "__main__":
    main()
