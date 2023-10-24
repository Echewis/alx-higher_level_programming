#!/usr/bin/python3
"""Define the square """


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            """Condition to check for integer """
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must br >= 0")
            """This will raise error message """
        self.__size = size
