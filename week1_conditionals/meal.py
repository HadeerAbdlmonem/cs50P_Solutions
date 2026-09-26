"""Determine which meal (breakfast, lunch, or dinner) corresponds to a given time of day."""

from sys import exit


def main():
    time_str = input("Time: ").strip()
    hours, minutes = time_str.split(":")
    total_minutes = int(hours) * 60 + int(minutes)

    if 7 * 60 <= total_minutes <= 8 * 60:
        print("Breakfast time")
    elif 12 * 60 <= total_minutes <= 13 * 60:
        print("Lunch time")
    elif 18 * 60 <= total_minutes <= 19 * 60:
        print("Dinner time")
    else:
        exit()


if __name__ == "__main__":
    main()
