#!/usr/bin/python3
"""
 This module opens a url and gets the response
"""

import urllib.request


def fetch():
    """
        fetch data from a given url
    """
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        res = 'Body response:\n\t- type: <class \'bytes\'>\n\t- content: {}\n\t- utf8 content: OK'.format(
            body)
        print(res)


if __name__ == '__main__':
    fetch()
