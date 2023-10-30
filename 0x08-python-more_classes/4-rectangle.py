#!/usr/bin/python3
"""class initialization """


class Rectangle:
    """class difinition """
    def __init__(self, width=0, height=0):
        """class definnition
        Args:
            width: the rectangle width
            height: rectangles height
        Raise:
            TypeError: if the value is not an integer
            ValueError: if the value is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """will get the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """will get the height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """will get the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """definition of area """
        return (self.__width * self.__height)

    def perimeter(self):
        """definition of perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """definition of string"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rectangle = ""
        for vertical in range(self.__height):
            for horizontal in range(self.__width):
                rectangle += "#"
            if vertical < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """definition of repr """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
