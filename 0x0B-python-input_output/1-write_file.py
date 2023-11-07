#!/usr/bin/python3
""" This is a function that writes to the string(utf8) """


def write_file(filename="", text=""):
    """definition of funtion write_file"""

    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
