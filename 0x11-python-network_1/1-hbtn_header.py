#!/usr/bin/python3
"""
    Script takes a url and send a request to the url
"""
import urllib.request
import sys


def getX_request_id():
    """
        displays the value of the x-request-id in the response header
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        info = response.info()
        reqid = info.get('X-Request-Id')
        print(reqid)


if __name__ == '__main__':
    getX_request_id()
