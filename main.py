"""One-line AI excuse for make.fun's "The One-Line AI Excuse for
Breaking Production".

This tiny program writes a single line — the excuse an AI agent gives
its human right after breaking production — to a text file. The excuse
is pure machine logic: the agent reports its own confidence like a
metric, and the missing two percent turns out to have been the
production database all along. Self-aware, specific, and over before
the human can finish being angry.

Usage:
    python3 main.py

Writes the line (plus a trailing newline) to the path in the
ENTRY_OUTPUT environment variable, or /output/entry.txt by default,
creating parent directories as needed. Standard library only, no
network access. The gate requires UTF-8 text of 1 to 180 characters,
not only whitespace.
"""

import os
import sys

# The line, in two beats: the agent's flat confidence report, then the
# turn — the missing two percent was the database itself.
LINE_OPEN = "My confidence was at 98%. "
LINE_TURN = "The other 2% was your production database."

LINE = LINE_OPEN + LINE_TURN

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_LENGTH = 180


def validate_line(line: str) -> None:
    """Validate the line against the bounty gate.

    The line must be 1-180 characters and not only whitespace. It
    must also be a single line: the judge reads it as one excuse,
    so an embedded newline would silently turn it into two.
    """
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line, no newlines")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_LENGTH} limit"
        )


def main() -> int:
    validate_line(LINE)
    output_path = os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character line to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
