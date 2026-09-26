"""A simple math quiz: generate addition problems at a chosen difficulty level."""

from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        score += ask_question(x, y)
    print(f"Your result is {score}/10")


def ask_question(x, y):
    prompt = f"{x} + {y} = "
    for attempt in range(3):
        answer = input(prompt)
        try:
            if int(answer) == x + y:
                return 1
        except ValueError:
            print("EEE")
        if attempt == 2:
            print(x + y)
    return 0


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass
        print("Enter a valid number for level")


def generate_integer(level):
    if level == 1:
        return randint(0, 9), randint(0, 9)
    elif level == 2:
        return randint(10, 99), randint(10, 99)
    else:
        return randint(100, 999), randint(100, 999)


if __name__ == "__main__":
    main()
