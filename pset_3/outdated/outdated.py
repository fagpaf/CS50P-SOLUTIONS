def main():
    format_date()


def format_date():
    month_of_year = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    while True:
        date = input("Date: ")
        if "/" in date:
            boolean = intenger_date(date, month_of_year)
            if boolean != False:
                return

        elif "," in date:
            boolean = string_date(date, month_of_year)
            if boolean != False:
                return


def intenger_date(date, month_of_year):
    new_date = date.split("/")
    month, day, year = new_date # Desse modo desempacota a lista como exemplo: ['9', '8', '1636']

    if month in month_of_year:
        return False

    month = int(month)
    day = int(day)
    year = int(year)

    if day > 31 or month > 12:
        return False

    print(f"{year}-{month:02}-{day:02}")

    return True


def string_date(date, month_of_year):
    new_date = date.split(" ")
    month, day, year = new_date # Desse modo desempacota a lista como exemplo: ['September', '8,', '1636']
    day = day.replace(",", "")

    try:
        month = month_of_year[month]
        day = int(day)
        year = int(year)

        if day > 31:
            return False

        print(f"{year}-{month:02}-{day:02}")
        return True
    except:
        return False


if __name__ == "__main__":
    main()
