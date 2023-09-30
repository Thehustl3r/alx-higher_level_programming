#!/usr/bin/python3
""" this function will reveal 10 latest commit from a github acc"""
from requests import get, codes
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    data = {'owner': owner, 'repo': repo}

    response = get(url)

    try:
        objects = response.json()
        for i, obj in enumerate(objects):
            print('{}: {}'.format(obj.get('sha'),
                                  obj.get('commit').get('author')
                                  .get('name')))
            if i == 9:
                break
    except ValueError:
        pass
