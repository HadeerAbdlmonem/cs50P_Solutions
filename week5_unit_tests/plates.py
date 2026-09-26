"""Validate whether a string could be a legal vanity license plate."""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s.isalnum():
        return False
    if not s[0].isalpha():
        return False
    if s.isalpha():
        return True

    first_digit_index = next(i for i, char in enumerate(s) if char.isdigit())
    if s[first_digit_index] == "0":
        return False
    return s[first_digit_index:].isdigit()


if __name__ == "__main__":
    main()
