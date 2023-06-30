#!/usr/bin/python3
"""
    uses query params to send data to endpoint
"""
import requests
import sys


def sendrequest(param=""):
    """
    sends a request with query params to given url
    """
    url = 'http://0.0.0.0:5000/search_user'
    payload = {}
    payload['q'] = param

    resp = requests.post(url, data=payload)

    try:
        data = resp.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.id, data.name))
    except Exception:
        print("Not a valid json")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        sendrequest(sys.argv[1])
    else:
        sendrequest()
