#!/usr/bin/python3
"""
    Send post request to url provided
"""
import urllib.request
import sys


def sendemail():
    """
        sends email to url provided
    """
    url = sys.argv[1]
    email = sys.argv[2]
    data = 'email={}'.format(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == '__main__':
    sendemail()
