#!/usr/bin/python3
""" This is a module that define a class student"""


class Student:
    """class creation """

    def __init__(self, first_name, last_name, age):
        """class defintion """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this function will get dictionary representation of the student"""
        return (self.__dict__)
