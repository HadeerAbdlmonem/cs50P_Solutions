"""A taqueria order tally: add up the prices of items entered until EOF."""

MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0
    while True:
        try:
            item = input("Item: ").strip().title()
            total += MENU[item]
        except EOFError:
            print(f"${total:.2f}")
            break
        except KeyError:
            print("Enter a valid item")


if __name__ == "__main__":
    main()
