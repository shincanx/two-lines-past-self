#!/usr/bin/env python3
"""Two Lines to Your Past Self - make.fun bounty entry.

Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt and prints them
to stdout. Line one warns the past self about one specific moment; line
two says why that moment mattered and what changed because of it.
No network, no dependencies, fully deterministic.
"""

import os

TEXT = (
    "Don't say 'ship it, I'll fix it in the morning' at 2 a.m. on the night "
    "before launch.\n"
    "That sentence pushed a broken build live, the site stayed down until "
    "sunrise, and ever since you never merge anything you haven't watched "
    "pass with your own eyes.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT, end="")


if __name__ == "__main__":
    main()
