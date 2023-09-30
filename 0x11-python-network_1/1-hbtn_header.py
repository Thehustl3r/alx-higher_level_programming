#!/usr/bin/python3
""" this module tends to fetch data from url"""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    header = response.info()['X-Request-Id']
    print(header)
