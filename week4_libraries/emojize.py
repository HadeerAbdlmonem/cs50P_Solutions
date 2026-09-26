"""
Convert emoji shortcodes typed by the user into emoji characters.
Example codes: :thumbs_down:, :thumbs_up:, :money_bag:, :1st_place_medal:, :angry_face:, :thinking_face:
"""

import emoji


def main():
    text = input("Input: ")
    print("Output:", emoji.emojize(text))


if __name__ == "__main__":
    main()
