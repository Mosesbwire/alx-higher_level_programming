#!/usr/bin/python3
"""
 Makes a post request to provided url
"""
import requests
import sys


def sendemail(url, address):
    """
    makes a post request to url
    """
    data = {}
    data['email'] = address
    resp = requests.post(url, data=data)
    print(resp.text)


if __name__ == '__main__':
    url = sys.argv[1]
    address = sys.argv[2]
    sendemail(url, address)
