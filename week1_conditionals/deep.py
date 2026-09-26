"""Ask the ultimate question of life, the universe, and everything."""


def main():
    answer = input("Answer: ").lower().strip()
    if answer in ("42", "forty two", "forty-two"):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
