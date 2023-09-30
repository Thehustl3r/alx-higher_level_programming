#!/usr/bin/python3
""" this module tends to fetch data from database """
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))
