"""Validate whether the user has entered a properly formatted email address."""

from validators import email


def main():
    email_address = input("What's your email address? ")
    if email(email_address):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
