import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv)!= 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_ext = input_path.lower().rsplit(".", 1)
    output_ext = output_path.lower().rsplit(".", 1)

    if len(input_ext)!= 2 or input_ext[1] not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid input")
    if len(output_ext)!= 2 or output_ext[1] not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid input")
    if input_ext[1]!= output_ext[1]:
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt image not found")

    input_cropped = ImageOps.fit(input_image, shirt.size)

    input_cropped.paste(shirt, shirt)

    input_cropped.save(output_path)

if __name__ == "__main__":
    main()
