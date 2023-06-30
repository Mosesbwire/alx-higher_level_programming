#!/usr/bin/python3
"""
    uses the requests package to make http calls
"""
import requests


def fetch():
    """
        makes a get request to provided url and display response body
    """
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)
    s = 'Body response:\n\t- type: <class \'str\'>\n\t- content: {}'.format(
        resp.text)
    print(s)


if __name__ == '__main__':
    fetch()
