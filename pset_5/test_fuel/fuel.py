import sys


def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        # Caso caia em uma exceção
        if percentage is False:
            continue

        result = gauge(percentage)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{result:.0f}%")
        sys.exit(0)


def convert(fraction):
        try:
            numerator, denominator = map(int, fraction.split("/"))
            if numerator <= denominator:
                pct = (numerator/denominator) * 100
                return pct
            else:
                return False

        except ZeroDivisionError:
            return -1
        except ValueError:
            return False


def gauge(pct):
    if pct >= 99:
        return "F"
    elif pct <= 1:
        return "E"
    else:
        return pct


if __name__ == "__main__":
    main()
