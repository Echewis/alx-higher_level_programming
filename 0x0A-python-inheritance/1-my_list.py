#!/usr/bin/python3
"""The file will inherit from the list class """


class MyList(list):
    """Creation of class MyList"""
    def print_sorted(self):
        """This will print a sorted list"""
        print(sorted(self))
