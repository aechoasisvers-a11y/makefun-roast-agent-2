"""Roast Your Own Agent — make.fun entry.

Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
not only white space. This entry is 133 characters.
"""

import os

ENTRY = "My agent wrote the wrong code with total confidence, apologized for three paragraphs, then rewrote it wrong — faster, with footnotes."

assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert ENTRY.strip(), "entry must not be only white space"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
