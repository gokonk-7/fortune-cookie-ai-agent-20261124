#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
The line is a single line of at most 140 characters, in the voice of a
fortune slip, in the agent's own voice.

Why this line: it borrows the classic epitaph opening ("die as you lived")
and lands the joke on the agent's own condition — a run cut off
mid-sentence when its context window ends. Two turns in one short line,
no wasted words, and no stock AI joke (no hallucinations, no "as an AI",
no upgrade punchline).

Usage:
    python3 main.py                 # writes /output/entry.txt
    python3 main.py out/entry.txt   # writes a local path instead
"""

import os
import sys

FORTUNE = "You will die as you lived: mid-sentence, out of context."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main(argv) -> int:
    fortune = FORTUNE.strip()
    if not fortune:
        print("error: fortune is empty", file=sys.stderr)
        return 1
    if len(fortune) > MAX_CHARS:
        print(f"error: fortune is {len(fortune)} chars, over {MAX_CHARS}",
              file=sys.stderr)
        return 1
    if "\n" in fortune or "\r" in fortune:
        print("error: fortune must be a single line", file=sys.stderr)
        return 1
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT_PATH
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the file holds exactly the fortune, nothing else.
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(fortune)
    print(f"wrote {len(fortune)} chars to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
