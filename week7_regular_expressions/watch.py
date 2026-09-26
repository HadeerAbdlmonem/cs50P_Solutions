"""Extract a shareable youtu.be link from an embedded YouTube iframe snippet."""

import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    match = re.search(
        r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/(\w+)".*</iframe>',
        html,
    )
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
