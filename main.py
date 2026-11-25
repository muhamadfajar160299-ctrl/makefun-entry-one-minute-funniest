#!/usr/bin/env python3
"""One-line entry runner.

Reads entry.txt shipped next to this script and copies it byte-identically
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), mode 0644, with no
temporary file. Stdlib only.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not data or not data.strip():
        print("entry.txt is empty", file=sys.stderr)
        return 1
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.txt")
        with open(dst, "wb") as f:
            f.write(data)
        os.chmod(dst, 0o644)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
