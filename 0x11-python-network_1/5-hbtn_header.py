#!/usr/bin/python3
"""
    Sends request to a url displays response header values
"""
import requests
import sys


def displayrequestid():
    """
        sends request to url the print the request-id of the response
    """
    url = sys.argv[1]
    resp = requests.get(url)
    print(resp.headers.get('X-Request-Id'))


if __name__ == '__main__':
    displayrequestid()
