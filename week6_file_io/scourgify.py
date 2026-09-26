"""Convert a CSV of 'Last, First' names + house into a CSV with First, Last, House columns."""

import csv
from sys import argv, exit


def main():
    if len(argv) != 3:
        exit("Usage: python scourgify.py input.csv output.csv")

    try:
        with open(argv[1]) as infile, open(argv[2], "w", newline="") as outfile:
            reader = csv.reader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for name, house in reader:
                last, first = name.split(", ")
                writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        exit("File does not exist")


if __name__ == "__main__":
    main()
