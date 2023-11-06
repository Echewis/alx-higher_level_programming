#!/usr/bin/python3
""" intialization of function inherits_from """


def inherits_from(obj, a_class):
    """ definition of function """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)

