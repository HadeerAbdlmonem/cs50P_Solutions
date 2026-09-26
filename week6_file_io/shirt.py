"""Overlay a shirt image onto a photo (CS50P 'Shirt' exercise).

NOTE: the image-processing logic itself is still a work in progress in the
original submission; only the file-handling scaffold has been cleaned up here.
"""

from sys import argv, exit


def main():
    if len(argv) != 3:
        exit("Usage: python shirt.py input.jpg output.jpg")

    try:
        with open(argv[1], "r"):
            pass  # TODO: read and process the input image

        with open(argv[2], "w"):
            pass  # TODO: write the composited output image
    except Exception:
        exit("Could not open input/output file")


if __name__ == "__main__":
    main()
