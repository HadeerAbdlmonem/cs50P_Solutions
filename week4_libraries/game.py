"""A number-guessing game: guess a random number between 0 and a chosen level."""

from random import randint
from sys import exit


def main():
    level = get_level()
    number = randint(0, level)

    while True:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            exit()

        if guess < 0:
            continue
        elif guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            exit()


if __name__ == "__main__":
    main()
