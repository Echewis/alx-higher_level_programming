#!/usr/bin/python3
"""

This module handles division

"""


def matrix_divided(matrix, div):
    """ Its a function that divides numbers

    Parameters:
        matrix: it is the list of integers
        div: it is the number that divides the matrix

    Return:
        it will return a new matrix

    Raises:
        TypeError: if the value is not an integer or float, not listed
        ,not same size
    ZeroDivisionError: if div is 0


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/float"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    e_len = 0
    size_msg = "Each row of the matrix must have the same size"

    for things in matrix:
        if not things or not isinstance(things, list):
            raise TypeError(msg_type)

        if e_len != 0 and len(things) != e_len:
            raise TypeError(size_msg)

        for number in things:
            if not type(number) in (int, float):
                raise TypeError(msg_type)

        e_len = len(things)

    z = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (z)
