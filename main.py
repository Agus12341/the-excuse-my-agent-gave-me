#!/usr/bin/env python3
"""Write the agent's excuse to entry.txt in the output folder."""

import os

# The gate checks entry.txt as UTF-8 text of 1 to 200 characters: this
# excuse is 81 code points, one line, delivered completely straight-faced.
TEXT = "I didn't miss the deadline. I hallucinated a later one, with complete confidence."


def write_entry(out_dir: str) -> None:
    """Write the excuse, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
