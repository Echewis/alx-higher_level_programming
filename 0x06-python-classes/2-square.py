#!/usr/bin/python3
"""Define the square """


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            """Condition to check for integer
            Args:
                size: the size of square
            Raises:
                TypeError: The type of error
                ValueError: error type
            """
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must br >= 0")
        self.__size = size
