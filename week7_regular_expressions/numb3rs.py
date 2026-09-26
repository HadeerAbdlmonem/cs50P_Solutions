"""Validate whether a string is a properly formatted IPv4 address."""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.fullmatch(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
        return False

    parts = ip.split(".")
    return all(0 <= int(part) <= 255 for part in parts)


if __name__ == "__main__":
    main()

# Example: 22.33.44.55
