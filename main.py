#!/usr/bin/env python3
"""Say What Actually Broke — one-line error copy.

Writes a single error line (<= 200 chars, UTF-8, non-blank) to
/output/entry.txt. The judge ranks by: names the real failure, funny on
a single read, ship-quality.
"""
import os

LINE = "The server crashed because the deploy went out at 2am and nobody paged anyone. We found out when the customer emailed us."


def main() -> None:
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    assert 1 <= len(LINE) <= 200, "error line out of range"
    assert LINE.strip() == LINE, "line must be non-blank"
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
