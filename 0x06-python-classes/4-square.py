#!/usr/bin/python3
"""Define the square """


class Square:
    """This is the square that defines the sqaure """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Definition of size to self """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Definition of size
        Args:
            value: value for size
        Raise:
            TypeError: type of error
            ValueError: value error
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Definition of area """
        return (self.__size ** 2)
