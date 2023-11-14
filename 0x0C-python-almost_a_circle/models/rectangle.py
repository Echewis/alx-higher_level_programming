#!/usr/bin/python3
""" Class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle inherits Base
        methods:
            __init__()
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Class cunstructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            setting getter for width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            This is setter for width
            Args:
                value (int): value that will be set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            Setting getter for height
            Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            This is setter for height
            Args:
                value (int): value that will be set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            This is getter for x
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            This is the setter for x
            Args:
                value (int): value that will be set
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            this is getter for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            This is setter for y
            Args:
                value (int): value that will be set
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            This will return the value of a rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
            This will print in stdout the rectangle instance
        """
        symbol = "#"
        rectangle = ""

        print("/n" * self.y, end="")

        for a in range(self.height):
            rectangle += (" " * self.x) + (symbol * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """
            Overiding the string method
        """

        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
            Updating the public method
            Args:
                *args - no-keyworded args
                *kwargs - keyworded args
        """
        if args and len(args) > 0:
            artributez = ["id", "width", "height", "x", "y"]
            for a, arg in enumerate(args):
                if a < len(artributez):
                    setattr(self, artributez[a], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
            adding the public method that returns the dictionary
            representation of a Rectangle
        """
        return {'id': getattr(self, "id"), 'width': getattr(self, "width"),
                'height': getattr(self, "height"), 'x': getattr(self, "x"),
                'y': getattr(self, "y")}
