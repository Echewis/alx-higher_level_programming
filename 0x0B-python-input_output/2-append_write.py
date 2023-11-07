#!/usr/bin/python3
""" This function will append a string at the end of a text file (uft-8)"""


def append_write(filename="", text=""):
    """ definition of function append_write """
    with open(filename, "a+", encoding="utf-8") as f:
        return (f.write(text))
