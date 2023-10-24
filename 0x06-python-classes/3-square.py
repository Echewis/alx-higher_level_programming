#!/usr/bin/python3
"""Definition of class """


class Square:
    """Class difinition of Square """
    def __init__(self, size=0):
        """Condition to check for integers
        Args:
            size: the size of square
        Raises:
            TypeError: data type error
            ValueError: error for value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Defintion of area """
        return (self.__size ** 2)
