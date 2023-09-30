#!/usr/bin/python3
""" this module tends to fetch data from database """
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    headerInfo = response.headers
    print(headerInfo.get('x-request-id'))
