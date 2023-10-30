#!/usr/bin/python3
"""class initialization """


class Rectangle:
    """class definition """
    def __init__(self, width=0, height=0):
        """Initializing rectangle
        Args:
            width: the width of rectangle
            height: the height of the rectangle
        Raise:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This will get the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """will set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """will get height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """this will set he width"""
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """definition of area"""
        return (self.__width * self.height)

    def perimeter(self):
        """definition of perimter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """Diagram for the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        angle = ""
        for vertical in range(self.__height):
            for horizontal in range(self.__width):
                angle += "#"
            if vertical < self.__height - 1:
                angle += "\n"
        return (angle)
