"""Replace :) and :( with emoji equivalents in the input text."""


def main():
    text = input("Text: ")
    print(convert(text))


def convert(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i] == ":" and i + 1 < len(text) and text[i + 1] == ")":
            result += "😂"
            i += 2
        elif text[i] == ":" and i + 1 < len(text) and text[i + 1] == "(":
            result += "😥"
            i += 2
        else:
            result += text[i]
            i += 1
    return result


if __name__ == "__main__":
    main()
