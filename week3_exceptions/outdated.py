"""Convert a date in 'month/day/year' or 'Month day, year' format into 'year-month-day'."""

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def main():
    while True:
        date = input("Date: ").strip()
        try:
            print(convert(date))
            break
        except (ValueError, IndexError):
            print("Enter a valid format, e.g. 9/8/1636 or September 8, 1636")


def convert(date):
    if "/" in date:
        month, day, year = date.split("/")
        month, day, year = int(month), int(day), int(year)
    elif "," in date:
        month_day, year = date.split(", ")
        month_name, day = month_day.split(" ")
        month = MONTHS.index(month_name.title()) + 1
        day, year = int(day), int(year)
    else:
        raise ValueError("Unrecognized date format")

    return f"{year}-{month:02}-{day:02}"


if __name__ == "__main__":
    main()
