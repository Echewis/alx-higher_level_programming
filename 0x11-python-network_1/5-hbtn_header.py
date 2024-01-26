#!/usr/bin/python3
"""This will displays the X-Request-Id header variable
of a request to a given URL.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
