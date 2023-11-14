#!/usr/bin/python3
"""  In the  this file, the class Square will inherit from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherites from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class cunstructor for square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """this is getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """
        This is the setter for size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updating using keyworded and non keyworded
        """
        if args and len(args) > 0:
            """if the args exist"""
            attributez = ["id", "size", "x", "y"]
            for a, arg in enumerate(args):
                if a < len(attributez):
                    """if the index is valid"""
                    setattr(self, attributez[a], arg)
        else:
            """if the args is empty """
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """will override the string method """
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                self.id, self.x, self.y, self.size))
