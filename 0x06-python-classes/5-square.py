#!/usr/bin/python3
"""Define the square """


class Square:
    """Class definition """
    def __init__(self, size=0):
        """Initialing The  square
        Args:
            size: size of square
        Raise:
            ValueError: if size is less than 0
            TypeError: if it's not int
        """
        self.size = size

    @property
    def size(self):
        """Setting the size of square """
        return (self._size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """will calculate the area of a square """
        return (self.size ** 2)

    def my_print(self):
        """this will print the square with '#' character """
        if self.size == 0:
            print()
        else:
            for a in range(self.size):
                print("#" * self.size)
