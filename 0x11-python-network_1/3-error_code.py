#!/usr/bin/python3
""" fetch code with errors"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
