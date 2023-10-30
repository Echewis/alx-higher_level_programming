#!/usr/bin/python3
"""class initialization """


class Rectangle:
    """class difinition """
    number_of_instances = 0
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
        Rectangle.number_of_instances += 1

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
        """Initializing area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Intializing perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """Diagram for rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        square = ""
        for var in range(self.__width):
            for hor in range(self.__height):
                square += "#"
            if var < self.__height - 1:
                square += "\n"
        return (square)

    def __repr__(self):
        """definition of repr """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """definition of del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
