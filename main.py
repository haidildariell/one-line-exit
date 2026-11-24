"""The One-Line Exit: write one funny one-line resignation letter."""

import os

LINE = "I quit: the iceberg I was hired to watch has moved on, and so have I."

def choose_line():
    """Pick the resignation line: a ship's lookout quits because the
    iceberg he was hired to watch has already left."""
    return LINE


def write_entry(path, line):
    """Write one line to path, creating its parent directory first."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    write_entry(output_path, choose_line())


if __name__ == "__main__":
    main()
