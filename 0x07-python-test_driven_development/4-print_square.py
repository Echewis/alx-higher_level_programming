#!/usr/bin/python3
"""

This module contains a function that prints a square with # character

"""


def print_square(size):
    """ definition of function

    parameters:
        size: size of square tobe printed

    Return:
        nothing

    Raisess:
        TypeError: if the size is not an int
        ValueError: if value is less than 0


    """

    if not isinstance(size, int):
        raise TypeError("size must ba an int")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        print("#" * size)
