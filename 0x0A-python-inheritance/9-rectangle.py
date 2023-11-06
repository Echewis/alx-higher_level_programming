#!/usr/bin/python3
"""class definition """
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """ class definition"""
    def __init__(self, width, height):
        """ intialization of funtion """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Thiswill return the area of a rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """str representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
