#!/usr/bin/python3
""" Class Rectangle that defines a rectangle """


class Rectangle:
    """ class attribute"""
    number_of_instances = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """initialiazation width and height"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter foe width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This is getter for  height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ This is the setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area is width * height"""
        return self.width * self.height

    def perimeter(self):
        """ this will check if width and height is = 0"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """check if width and height is 0"""
        if self.width == 0 or self.height == 0:
            return ""
        rowz = []
        for a in range(self.height):
            row = str(Rectangle.symbol) * self.width
            rowz.append(row)
        return "\n".join(rowz)

    def __repr__(self):
        """will return a string that contains the class"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """will delete the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """check rect_1 and rect_2"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """This will return the instance of a rectangle"""
        return cls(size, size)
