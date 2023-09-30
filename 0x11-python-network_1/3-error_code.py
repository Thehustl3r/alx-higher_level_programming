#!/usr/bin/python3
""" fetch code with errors"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    if (len(argv) != 2):
        exit(1)

    url = argv[1]
    with urlopen(url) as response:
        try:
            the_page = response.read().decode('utf-8')
            print(the_page)
        except HTTPError as e:
            print('Error code: {}'.format(e.code))
