#!/usr/bin/python3
""" Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    res = requests.post(url, data=val)
    print(res.text)
