#!/usr/bin/env python3
"""Weirdest Job Title entry.

Prints a single job title: a claims adjuster who investigates lost socks.

The joke is a real professional frame (insurance claims adjuster) applied
to the most universal mundane loss (one sock gone from the wash) — specific
enough to picture the person doing it, short enough to take in at a glance.
Stdlib only; prints to stdout and nothing else, no file I/O.
"""

TITLE = "Lost Sock Claims Adjuster"

# The gate requires 1-60 characters, non-whitespace, a single title.
MAX_TITLE_CHARS = 60


def main() -> int:
    if not 1 <= len(TITLE) <= MAX_TITLE_CHARS or not TITLE.strip():
        raise ValueError("title must be 1-60 non-whitespace characters")
    print(TITLE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
