"""Count the substantive lines of code in a Python file (ignoring comments, docstrings, and blank lines)."""

from sys import argv, exit


def main():
    if len(argv) != 2:
        exit("Usage: python lines.py filename.py")

    filename = argv[1]
    if not filename.endswith(".py"):
        exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        exit("File does not exist")

    code_lines = 0
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and not stripped.startswith('"'):
            code_lines += 1

    print(f"Number of lines: {code_lines}")


if __name__ == "__main__":
    main()
