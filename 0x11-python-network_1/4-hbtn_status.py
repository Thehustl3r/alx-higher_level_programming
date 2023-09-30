#!/usr/bin/python3
""" this module tends to fetch data from database """
from requests import get


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    html = get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
