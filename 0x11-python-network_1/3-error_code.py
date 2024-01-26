#!/usr/bin/python3
"""This will sends a request to a given URL and displays the response body.
"""
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as responsive:
            print(responsive.read().decode("ascii"))
    except urllib.error.HTTPError as encode:
        print("Error code: {}".format(encode.code))
