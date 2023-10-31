#!/usr/bin/python3
"""
this module contains functions that prints ones full name

"""


def say_my_name(first_name, last_name=""):
    """ function that prints first name and last name

    parametera:
        first_name: f n
        last_name: L N

    Return:
        nothing

    Raises:
        TypeError: if f n or L N is not a string


    """

    if type(first_name) is not str:
        raise TypeError("first name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
