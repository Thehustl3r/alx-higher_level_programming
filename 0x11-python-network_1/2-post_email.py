#!/usr/bin/python3
""" this module tends to fetch data from url"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if (len(argv) != 3):
    exit(1)

email = {'email': argv[2]}
url = argv[1]
email = urlencode(email)
email = email.encode('utf-8')
req = Request(url, email)
with urlopen(req) as response:
    the_page = response.read().decode('utf-8')
    print(the_page)
