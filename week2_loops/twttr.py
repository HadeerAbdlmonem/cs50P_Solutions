"""Remove vowels from the input text (like old Twitter's abbreviated names)."""


def main():
    text = input("Text: ")
    print(remove_vowels(text))


def remove_vowels(text):
    return "".join(letter for letter in text if letter.lower() not in "aeiou")


if __name__ == "__main__":
    main()
