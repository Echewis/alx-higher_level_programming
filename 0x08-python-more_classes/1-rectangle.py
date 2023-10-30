#!/usr/bin/python3
"""This is  class definition """


class Rectangle:
    """This is rectangle """

    def __init__(self, width=0, height=0):
        """This is the initialization of class rectangle
        Args:
            width: the width of the class
            height: the height of the class
        Raise:
            TypeError: if the value type in not integer
            ValueError: if value is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Initializing the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting the value for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Initializing height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting value for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
