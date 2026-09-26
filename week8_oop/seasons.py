"""Compute how many minutes old someone is, spelled out in words."""

import re
from datetime import date
from sys import exit

from inflect import engine


def main():
    birth_date_str = input("Your birth date: ")

    if not re.fullmatch(r"\d{4}-\d{1,2}-\d{1,2}", birth_date_str):
        exit("Invalid birth date syntax")

    year, month, day = (int(part) for part in birth_date_str.split("-"))

    if not (1 <= month <= 12) or not (1 <= day <= 31):
        exit("Date out of range")

    birth_date = date(year, month, day)
    minutes = (date.today() - birth_date).days * 24 * 60

    p = engine()
    print(p.number_to_words(minutes, andword="") + " minutes")


if __name__ == "__main__":
    main()
