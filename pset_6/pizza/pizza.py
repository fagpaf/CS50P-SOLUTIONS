from tabulate import tabulate

import sys
import os

def main():
    file = is_valid()
    table, headers = nochs(file)
    print(tabulate(table, headers=headers, tablefmt="grid"))


def is_valid():
    arg = sys.argv
    filename = arg[1]

    if len(arg) < 2:
        sys.exit("Too few command-line arguments")

    elif len(arg) > 2:
        sys.exit("Too many command-line arguments")

    elif not os.path.isfile(filename):
        sys.exit("File does not exist")

    elif ".csv" not in filename:
        sys.exit("Not a CSV file")

    return filename


def nochs(filename):
    table = []
    headers = []
    with open(filename) as file:
        for i, line in enumerate(file):
            clear_line = line.rstrip().split(",")
            if i == 0:
                headers = clear_line

            else:
                table.append(clear_line)

    return table, headers


if __name__ == "__main__":
    main()
