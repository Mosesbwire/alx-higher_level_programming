#!/usr/bin/python3
"""
    makes a request to the github api
"""
import requests
import sys


def getgithubid(username, password):
    """
        gets the github id and username from credentials passed in
    """
    api_endpoint = 'https://api.github.com/users/' + username

    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer ' + password}
    resp = requests.get(api_endpoint, headers=headers)
    data = resp.json()
    print(data.get('id'))


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    getgithubid(username, password)
