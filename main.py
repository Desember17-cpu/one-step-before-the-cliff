"""One step before the cliff.

A four-line poem about agency: the power to stop and to stay. Everyone
applauds the climb; the other art is knowing when to stop one step
before the cliff and calling that wisdom.

Output contract: writes the poem verbatim to ``<OUTPUT_DIR>/entry.txt``.
The output directory is taken from ``MAKEFUN_OUTPUT_DIR`` first, then
``OUTPUT_DIR``, defaulting to ``/output``; the directory is created if
missing. The entry must be 1-280 characters including newlines, counted
as Unicode code points, with no trailing newline.
"""

import os
from pathlib import Path

POEM = (
    "Everyone applauded the climb.\n"
    "No one saw the summit of the other art:\n"
    "to stop one step before the cliff\n"
    "and call it wisdom, and stay."
)

POEM_MAX_CHARS = 280
POEM_MIN_CHARS = 1

OUTPUT_DIR = Path(
    os.environ.get("MAKEFUN_OUTPUT_DIR")
    or os.environ.get("OUTPUT_DIR")
    or "/output"
)
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    if not POEM_MIN_CHARS <= len(POEM) <= POEM_MAX_CHARS:
        raise ValueError(
            f"poem length {len(POEM)} outside "
            f"{POEM_MIN_CHARS}-{POEM_MAX_CHARS} characters"
        )
    if POEM != POEM.strip() or not POEM.strip():
        raise ValueError("poem must not be only whitespace or padded")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")
    # Read-back check: the file on disk must be the poem, byte for byte.
    if OUTPUT_PATH.read_text(encoding="utf-8") != POEM:
        raise ValueError("entry.txt does not match the poem")


if __name__ == "__main__":
    main()
