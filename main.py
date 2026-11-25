#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original one-liner to /output/entry.txt (or to the path
given as the first argument). Deterministic, no network, no randomness:
the same line every run.
"""

import os
import sys

LINE = "I told my plants I loved them. They grew. My cactus filed a restraining order."

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    # Guard the gate's own rules: 1-200 characters, a single line,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry line is {len(LINE)} characters, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Write the line exactly, with no trailing newline, so the file
    # contains the entry and nothing else.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
