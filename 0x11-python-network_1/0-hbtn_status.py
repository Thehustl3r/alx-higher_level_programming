#!/usr/bin/python3
""" this module tends to fetch data from database """
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    body = response.read()
    print(body)
