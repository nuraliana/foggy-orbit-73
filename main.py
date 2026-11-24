#!/usr/bin/env python3
"""Write the selected one-line alien tourist review of Earth to entry.txt.

Stdlib only. Output directory is MAKEFUN_OUTPUT_DIR (default ".").
"""

import os

ENTRY = (
    "They carry tiny folding roofs for when the sky leaks, "
    "then lose them immediately. 4/5 \u2014 the rain, at least, is honest."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry is {len(text)} characters, over the 200 limit"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
