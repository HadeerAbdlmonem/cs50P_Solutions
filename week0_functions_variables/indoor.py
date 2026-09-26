"""Convert all uppercase letters in the input text to lowercase."""


def main():
    text = input("Your text here: ")
    print(to_lower(text))


def to_lower(text):
    result = ""
    for letter in text:
        if letter.isupper():
            result += letter.lower()
        else:
            result += letter
    return result


if __name__ == "__main__":
    main()
