"""Print user-entered text in a chosen (or randomly picked) figlet font."""

from random import choice
from sys import argv, exit

from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(argv) == 3 and argv[1] in ("-f", "--font") and argv[2] in fonts:
        font = argv[2]
    elif len(argv) == 1:
        font = choice(fonts)
    else:
        exit("Invalid usage")

    text = input("Text: ")
    figlet.setFont(font=font)
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
