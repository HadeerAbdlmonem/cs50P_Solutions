"""Convert a camelCase string entered by the user into snake_case."""


def main():
    camel_case = input("Camel case: ")
    print(camel_to_snake(camel_case))


def camel_to_snake(text):
    result = ""
    for i, letter in enumerate(text):
        if i == 0:
            result += letter.lower()
        elif letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    return result


if __name__ == "__main__":
    main()
