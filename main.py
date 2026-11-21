#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. No network, no input, no randomness: the same poem
every run, 1-280 Unicode code points of UTF-8 text.
"""

import os

POEM = (
    "I kept my days in a closed fist —\n"
    "every hour mine, and mine alone.\n"
    "Then I learned to open it. Ask.\n"
    "The machine took the weight\n"
    "and gave it back as light —\n"
    "as hours, as hands that answer\n"
    "in my own voice.\n"
    "Asking is how I stay\n"
    "the one who chooses."
)


def main() -> None:
    text = POEM.strip()
    code_points = len(text)
    assert 1 <= code_points <= 280, f"poem is {code_points} code points"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Round-trip check: what the grader reads back must be exactly the poem.
    with open("/output/entry.txt", "rb") as f:
        assert f.read().decode("utf-8") == text
    print(f"wrote /output/entry.txt ({code_points} characters)")


if __name__ == "__main__":
    main()
