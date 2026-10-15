import csv
import sys
import os

def main():
    before, after = is_valid()
    convert(before, after)


def is_valid():
    arg = sys.argv
    if len(arg) < 3:
        sys.exit("Too few command-line arguments")

    read_csv = arg [1]
    write_csv = arg[2]
    if len(arg) > 3:
        sys.exit("Too many command-line arguments")

    elif not os.path.isfile(read_csv):
        sys.exit("Could not read invalid_file.csv")

    return read_csv, write_csv


def convert(read_csv, write_csv):
    students = []

    with open(read_csv) as before:
        reader = csv.DictReader(before)
        for row in reader:
            # row["name"] vem no formato "Sobrenome, Nome"
            last, first = row["name"].split(", ")
            house = row["house"]
            students.append({"first": first, "last": last, "house": house})

    with open(write_csv, "w", newline="") as after:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(after, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
