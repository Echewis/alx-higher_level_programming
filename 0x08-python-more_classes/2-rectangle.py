#!/usr/bin/python3
"""This is initialization of class """


class Rectangle:
    """Definition of class """
    def __init__(self, width=0, height=0):
        """Initializing the rectangle
        Args:
            width: This is the width
            height: this the height
        Raise:
            TypeError: if the value is not an integer
            VAlueError: if the value is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This gets the  width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ This will set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This will get the height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """This will set the value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Sets the area of the width and height """
        return (self.__width * self.__height)

    def perimeter(self):
        """Definition of perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
