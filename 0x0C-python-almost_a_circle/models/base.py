#!/usr/bin/python3
"""This is a base class """
import json
import turtle
import csv


class Base:
    """ class creation base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            initialization of class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Retuens The JSON serialization

        Args:
            list_dictionary (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dump(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This will write to json serialization

        Args:
            list_objs (list): inherited base instance
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Return json string
        Args:
            json_string (str): JSON string representation
        Returns:
            an empty list if json_string is Nonenor empty
        """
        if json_string in None or json_string == "[]":
            return []
        return json.load(json_string)
