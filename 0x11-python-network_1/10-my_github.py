#!/usr/bin/python3
""" this module tends to fetch data from database """
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    passwd = argv[2]
    response = get(url, auth=HTTPBasicAuth(username, passwd))
    try:
        obj = response.json()
        print(obj.get('id'))
    except ValueError:
        print(None)
