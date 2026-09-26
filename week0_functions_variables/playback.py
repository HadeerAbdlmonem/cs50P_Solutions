"""Replace spaces in the input text with '...'."""


def main():
    text = input("Enter your text here: ")
    print(convert(text))


def convert(text):
    return text.replace(" ", "...")


if __name__ == "__main__":
    main()
