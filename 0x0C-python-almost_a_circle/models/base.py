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
        return json.dumps(list_dictionaries)

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
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class instance from a dictionary
        """
        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                fresh = cls(1, 1)
            else:
                fresh = cls(1)
            fresh.update(**dictionary)
            return fresh

    @classmethod
    def load_from_file(cls):
        """
        class instance from a file of Jason
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serialisation of csv list
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs in None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    writer = csv.DictWritter(csvfile, fieldnames=fieldnames)
                    for o in list_objs:
                        writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_csv(cls):
        """
        This is the list of classes That was instantiated from csv file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, filename=fieldnames)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Will draw a rectangle and square using turtle module
        Args:
            list_rectangle (list): a list of rectangle to draw
            list_square (list): List of square to be draw
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for a in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
                turt.hideturtle()

        turt.color("#b5e3d8")
        for s in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(s.x, s.y)
            turt.down()
            for a in range(2):
                turt.forward(s.width)
                turt.left(90)
                turt.forward(s.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitoniclick()
