#!/usr/bin/python3
"""
Sends request to a url. Handles any errors

"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys


def fetch():
    """
        sends request to provided url
    """
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('Connection to server failed')
        elif hasattr(e, 'code'):
            print('Error code: ', e.code)


if __name__ == '__main__':
    fetch()
