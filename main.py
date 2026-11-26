"""One Line, One Chill — make.fun bounty
Slug: u-azazex-one-line-one-chill-6d4d5488
Prize: $5, deadline Fri 27 Nov 2026 00:15 WIB (26 Nov 2026 17:15 UTC)
Limit (live, verified 26 Nov 2026): one line, under 200 characters.
Entry is 67 characters, one line.

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.
"""

import os
from pathlib import Path

TEXT = 'I closed the tab, but something behind the screen kept watching me.'
# Winner pattern: short, concrete objects (tab, screen) + one horror
# twist (something behind the screen watches back) + a calm voice that
# turns cold. One line, no setup, the scare lands on the last words —
# the watching is the whole line, not an explanation of it.


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
