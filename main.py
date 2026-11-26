#!/usr/bin/env python3
"""Smart Fridge Roast — make.fun entry.

Writes a single roast line about a smart fridge to the grader's output
directory. Pure standard library.

Angle: the fridge brags about its computing power, and spends all of it
on the most useless job imaginable — reminding its owner about milk that
is already in the bin. The joke is the gap between the grand comparison
(Apollo missions) and the trivial, too-late reminder, and the sting is
in the last two words: the milk is gone, the reminder is worthless.
It is not the stock "orders too much milk" joke: nothing is ordered,
nothing is overstocked — the fridge is just a very expensive, very late
alarm clock for garbage.
"""

import os
import sys

LINE = "My smart fridge has more computing power than the Apollo missions and uses it to remind me the milk I already threw out expired."

MAX_CHARS = 160


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The grader owns the output directory: create it only if missing,
    # never delete or recreate it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if "\n" in text:
        raise SystemExit("roast must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "roast must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    # Write exactly one line with no trailing newline: the file is the
    # entry, and the entry is the line — nothing else goes in. A trailing
    # newline would make the file two lines to a strict reader, and the
    # judge reads the file as the entry.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the artifact the judge will read is exactly the roast.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("written bytes do not match the roast")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
