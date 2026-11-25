"""One-line office joke entry for the make.fun bounty.

Writes the joke line to /output/entry.txt (no trailing newline) and
prints it to stdout. Deterministic, stdlib only.

The joke: setup (fire drill interrupts a performance review) + turn
(the whole office finally agrees on the "exit strategy" — the fire
exit, and quitting). Punchline last, 138 chars, one line.
"""

from pathlib import Path

LINE = "The fire drill went off during my performance review, and for the first time all year, everyone in the office agreed on the exit strategy."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def validate(line):
    """Gate: 1-200 chars, single line, no leading/trailing whitespace."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line must be 1-200 chars")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must have no leading/trailing whitespace")


def main():
    validate(LINE)
    OUTPUT_PATH.write_bytes(LINE.encode("utf-8"))  # byte-exact, no newline
    print(LINE)


if __name__ == "__main__":
    main()
