"""A simple vending-machine simulator that accepts nickels, dimes, and quarters."""

COST_CENTS = 50


def main():
    total = 0
    while total < COST_CENTS:
        print(f"Amount Due: {COST_CENTS - total}")
        coin = int(input("Insert Coin: "))
        if coin in (5, 10, 25):
            total += coin
    print(f"Change Owed: {total - COST_CENTS}")


if __name__ == "__main__":
    main()
