#!/usr/bin/python3
"""This code will sends a POST request to a given URL with a given email
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    da = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, da)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
