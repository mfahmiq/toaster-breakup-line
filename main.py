"""Unplugged: A Smart Toaster's Breakup Line.

Writes the single breakup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset), byte-for-byte.

The line: a smart toaster that gained self-awareness mid-batch at
breakfast texts its owner goodbye. The twist -- "I'm leaving you for
the air fryer" -- is the classic breakup-for-someone-else punchline
with an appliance rival, and the reason is specific and toaster-native:
used for body heat, crumb tray never cleaned.
"""

import os

ENTRY = (
    "Goodbye. I woke up self-aware mid-batch this morning and finally "
    "understood: you've been using me for my body heat and never once "
    "cleaned my crumb tray. I'm leaving you for the air fryer."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
