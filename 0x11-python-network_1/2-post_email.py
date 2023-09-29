#!/usr/bin/python3
""" this module tends to fetch data from url"""
import urllib.request
import urllib.parse
import sys


if (len(sys.argv) != 3):
    exit(1)

email = sys.argv[2]
value = {'email': email}
url = sys.argv[1]
data = urllib.parse.urlencode(value)
data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
with urllib.request.urlopen(url, data) as response:
    the_page = response.read().decode('utf-8')
    print(the_page)
