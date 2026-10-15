import sys
import os

"""Um programa que contabiliza quantas linhas de código escrito possui um arquivo .py"""

def main():
    file = is_valid()
    print(loc(file))


def is_valid():
    arg = sys.argv
    filename = arg[1]
    if len(arg) < 2:
        sys.exit("Too few command-line arguments")

    elif len(arg) > 2:
        sys.exit("Too many command-line arguments")

    elif ".py" not in filename:
        sys.exit("Not a Python file")

    elif not os.path.isfile(filename):
        sys.exit("File does not exist")

    return filename


def loc(filename):
    cnt = 0
    with open(filename) as file:
        for line in file:
            if line.lstrip().startswith("#") or line.strip() == "":
                continue
            else:
                cnt += 1
    return cnt


if __name__ == "__main__":
    main()
