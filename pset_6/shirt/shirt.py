from PIL import Image
from PIL import ImageOps

import sys
import os

def main():
    before, after = is_valid()
    costumes(before, after)


def is_valid():
    arg = sys.argv
    if len(arg) < 3:
        sys.exit("Too few command-line arguments")

    read_jpg = arg [1]
    write_jpg = arg[2]
    if len(arg) > 3:
        sys.exit("Too many command-line arguments")

    elif not write_jpg.lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    elif read_jpg[-3:] != write_jpg[-3:]:
        sys.exit("Input and output have different extensions")

    elif not os.path.isfile(read_jpg):
        sys.exit("Input does not exist")

    return read_jpg, write_jpg


def costumes(read_jpg, write_jpg):
    image = Image.open(read_jpg)
    shirt = Image.open("shirt.png")

    img_resize = ImageOps.fit(image, shirt.size)
    img_resize.paste(shirt, (0, 0), shirt)
    img_resize.save(write_jpg)


if __name__ == "__main__":
    main()
