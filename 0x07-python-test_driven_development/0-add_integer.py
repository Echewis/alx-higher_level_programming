#!/usr/bin/python3
"""

It ia a module that comprises of two function

"""


def add_integer(a, b=98):
    """Definition of function that adds two numbers

    parameters:
        a: first number
        b: second number

    Returns:
        The addition of the given number

    Raises:
        TypeError: If any of the variables is not an integer

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
