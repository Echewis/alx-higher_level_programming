#!/usr/bin/python3
""" initialization of class """


class BaseGeometry:
    """class defintion """

    def area(self):
        """ implementation not yet applied """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ will validate the value as an int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
