"""Convert an amount of bitcoin to US dollars using a live exchange-rate API."""

from sys import argv, exit

import requests


def main():
    if len(argv) != 2:
        exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        amount = float(argv[1])
    except ValueError:
        exit("Amount must be a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException:
        exit("Could not reach the exchange-rate API")

    rate = response.json()["bpi"]["USD"]["rate_float"]
    print(f"${amount * rate:,.4f}")


if __name__ == "__main__":
    main()
