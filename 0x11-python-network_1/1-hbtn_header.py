#!/usr/bin/python3
""" This will display X-Request-id"
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as respond:
        print(dict(respond.headers).get("X-Request-id"))
