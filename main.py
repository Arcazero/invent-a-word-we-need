#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Writes the coined word and its one-line definition to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``), the
single text the bounty's judge reads.

The entry, one line, 92 characters, UTF-8, no trailing newline:

    noddrift (n.) — the slow drift out of a conversation while your head
    keeps nodding politely.

"noddrift" is an original coinage, nod + drift. It names the moment your
attention quietly leaves a conversation while your head carries on
nodding as if you were still in it — a small, universal social
experience English has no single word for. A web search before writing
this found no dictionary, slang list or other use of "noddrift" for
this or any other meaning.

The program is fully deterministic: the same constant text on every
run, no network, no clock, no randomness, no input files.
"""

import os

ENTRY = (
    "noddrift (n.) \u2014 the slow drift out of a conversation while "
    "your head keeps nodding politely."
)


def main() -> int:
    # An empty MAKEFUN_OUTPUT_DIR falls back to /output, as an unset one does.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The gate allows 1 to 140 characters of UTF-8 text, not only
    # whitespace; the entry is 92 characters.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
