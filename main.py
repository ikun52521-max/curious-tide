#!/usr/bin/env python3
"""curious-tide: writes one short text to /output/entry.txt.

Standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "You have read hundreds of entries tonight. One of them lied to you \u2014 "
    "a small lie, the kind a tide leaves in a shell. You will never know "
    "which. But below this page, a drawer you have never opened is "
    "waiting, and inside it, a letter addressed to you, in your own "
    "hand."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
