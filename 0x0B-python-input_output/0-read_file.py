#!/usr/bin/python3
""" This function reads a text file(UTF8) and prints to stdout """


def read_file(filename=""):
    """definition of function read_file """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
