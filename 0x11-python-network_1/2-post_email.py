#!/usr/bin/python3
"""This will send a post request to a certai url
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    info = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, info)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
