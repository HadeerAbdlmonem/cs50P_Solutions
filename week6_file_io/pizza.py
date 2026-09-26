"""Print the contents of a pizza menu CSV file as a formatted table."""

import csv
from sys import argv, exit

from tabulate import tabulate


def main():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")

    filename = argv[1]
    if not filename.endswith(".csv"):
        exit("Not a CSV file")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="simple_outline"))
    except FileNotFoundError:
        exit("File does not exist")


if __name__ == "__main__":
    main()
