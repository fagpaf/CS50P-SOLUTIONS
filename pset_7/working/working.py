import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$", s)
    if not match:
        raise ValueError("Invalid time format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    if m1 == None:
        m1 = "00"
    if m2 == None:
        m2 = "00"

    h1 = int(h1)
    if p1 == "PM" and h1 != 12:
        h1 += 12
    elif p1 == "AM" and h1 == 12:
        h1 = 0

    h2 = int(h2)
    if p2 == "PM" and h2 != 12:
        h2 += 12
    elif p2 == "AM" and h2 == 12:
        h2 = 0

    return f"{h1:02}:{m1} to {h2:02}:{m2}"

if __name__ == "__main__":
    main()
