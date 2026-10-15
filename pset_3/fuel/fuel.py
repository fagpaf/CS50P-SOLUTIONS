def main():
    pct = is_valid()
    if pct >= 99:
        print("F")
    elif pct <= 1:
        print("E")
    else:
        print(f"{pct:.0f}%")


def is_valid():
    while True:
        try:
            fraction = input("Fraction: ")
            # Extrai os números e transforma para inteiro
            numerator, denominator = map(int, fraction.split("/"))
            if numerator <= denominator:
                pct = (numerator/denominator) * 100
                return pct
            else:
                pass
        except (ValueError, ZeroDivisionError): # Caso tenha erro avança no loop
            pass


main()
