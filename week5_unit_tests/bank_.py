"""Determine the greeting fee based on how a customer greets the cashier."""


def main():
    text = input("Your greeting: ").lower().strip()
    print(greeting(text))


def greeting(text):
    starts_with_h = text.startswith("h")
    starts_with_hello = text.startswith("hello")

    if starts_with_h and starts_with_hello:
        return "$0"
    elif starts_with_h and not starts_with_hello:
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
