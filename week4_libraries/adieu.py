"""Say adieu to a list of names entered by the user (Ctrl+D / Ctrl+Z to finish)."""


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            adieu(names)
            break


def adieu(names):
    """Print a farewell message that lists every name, e.g. 'Adieu, adieu, to A, B and C'."""
    print("Adieu, adieu, to ", end="")
    for i, name in enumerate(names):
        if i == len(names) - 1:
            print(f"and {name}", end="")
        else:
            print(f"{name}, ", end="")
    print()


if __name__ == "__main__":
    main()
