#!/usr/bin/python3
""" a module defines a class """


class MyInt(int):
    """ class definition"""

    def __eq__(self, value):
        """this will show override is equal to operator"""
        return (self.real != value)

    def __ne__(self, value):
        """ override is not equal to operator with equal to behaviour """
        return (self.real == value)
