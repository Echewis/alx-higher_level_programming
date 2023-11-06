#!/usr/bin/python3
""" basegeometry inheritance"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class defintion of Rectangle """

    def __init__(self, width, height):
        """ initialization of function"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
