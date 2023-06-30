#!/usr/bin/python3
"""
    sends request to url
    Handles errors
"""
import requests
import sys


def errorHandler(url):
    """
     prints the error status code if code >= 400
    """
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))


if __name__ == '__main__':
    url = sys.argv[1]
    errorHandler(url)
