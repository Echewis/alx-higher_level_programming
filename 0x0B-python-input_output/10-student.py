#!/usr/bin/python3
"""defintion of class student"""


class student:
    """class creation """

    def __init__(self, first_name, last_name, age):
        """Initializing a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function will get a dictionary representaion of student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {g: getattr(self, g) for g in attrs if hasattr(self, g)}
        return (self.)
