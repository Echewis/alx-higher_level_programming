#!/usr/bin/python3
""" module definition of a function """


def add_attribute(obj, att, value):
    """ defintion of add_attribute """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
