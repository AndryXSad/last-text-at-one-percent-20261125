"""Last Text at One Percent — make.fun entry.

Writes the final text message a dying phone sends at one percent
battery to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The message is fixed and deterministic: the same bytes on every run.
Standard library only, no network, no reads outside this file.
"""

import os

# The entry: one final text, in the dying phone's own voice.
# 75 characters, well under the 200-character gate.
MESSAGE = "1%. I held on at 3% for an hour just to watch you panic. Worth it. Goodbye."


def main() -> None:
    # Self-check the gate before writing: 1-200 chars, not only whitespace.
    if not 1 <= len(MESSAGE) <= 200 or not MESSAGE.strip():
        raise SystemExit("entry message fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts every character.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
