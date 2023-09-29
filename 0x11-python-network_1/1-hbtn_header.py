#!/usr/bin/python3
""" this module tends to fetch data from url"""
import urllib.request
import sys


if (len(sys.argv) != 2):
    exit(1)

url = '{}'.format(sys.argv[1])
with urllib.request.urlopen(url) as response:
    header = response.headers['X-Request-Id']
    print(header)
