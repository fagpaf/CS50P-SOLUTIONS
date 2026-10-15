import requests
import sys


def main():
    number = line_command()
    obj = query()

    price = float(obj["data"]["priceUsd"])
    amount = number * price
    print(f"${amount:,.4f}")


def line_command():
    if sys.argv == 1:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
        if n <= 0:
            raise ValueError
        return n

    except ValueError:
        sys.exit("Command-line argument is not a number")


def query():
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=11bb771e563e811d654fc9b2187c944a6482f099c6fd04ce5ec38d0569fe545c")
        return response.json()

    except requests.RequestException:
        sys.exit()


if __name__ == "__main__":
    main()
