from datetime import date

import inflect
import sys

def main():
    b_day = is_valid(input("Date of Birth: ").split("-"))
    days = age_in_minutes(b_day)
    p = inflect.engine()
    print(p.number_to_words(days, andword="").capitalize(), "minutes")


def is_valid(b_day):
    try:
        b_day = list(map(int, b_day))
        return b_day
    except ValueError:
        sys.exit("Invalid date")


def age_in_minutes(b_day):
    d1 = date.today()
    year, month, day = b_day
    d2 = date(year, month, day)

    dif = d1 - d2

    return dif.days * 24 * 60


if __name__ == "__main__":
    main()
