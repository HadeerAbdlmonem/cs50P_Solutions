"""Convert a range like '9 AM to 5 PM' into 24-hour military time, e.g. '9:00 to 17:00'."""

import re
from sys import exit


def convert(time_range):
    match = re.fullmatch(
        r"([1-9]|1[0-2])(:([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(:([0-5][0-9]))? (AM|PM)",
        time_range,
    )
    if not match:
        exit("Invalid input")

    hour1, _, minute1, period1, hour2, _, minute2, period2 = match.groups()
    print(f"{to_24_hour(hour1, minute1, period1)} to {to_24_hour(hour2, minute2, period2)}")


def to_24_hour(hour, minute, period):
    hour = int(hour)
    minute = minute or "00"

    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:  # PM
        hour = 12 if hour == 12 else hour + 12

    return f"{hour}:{minute}"


if __name__ == "__main__":
    convert(input("Hours: "))
