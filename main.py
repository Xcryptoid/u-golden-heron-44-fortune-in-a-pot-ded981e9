"""Fortune in a Pot — entrypoint.

Copies the pre-written fortune in entry.txt to the output directory.
Standard library only; nothing is rendered or generated at run time.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
