#!/usr/bin/python3
""" this module tends to fetch data from database """
from requests import post, code
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if (len(argv) > 1):
        q = {'q': argv[1]}
    else:
        q = {'q': ''}

    response = post(url, data=q)
    try:
        jsonObj = response.json()
        if len(jsonObj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(jsonObj['id'], jsonObj['name']))
    except:
        print('Not a valid JSON')
