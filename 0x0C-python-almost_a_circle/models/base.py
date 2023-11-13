#!/usr/bin/python3
"""This is a base class """


class Base:
    """ class creation base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
