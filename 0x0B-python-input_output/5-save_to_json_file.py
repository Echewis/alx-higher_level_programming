#!/usr/bin/python3
""" This function will write an object to a text file using json
representaion
"""
import json


def save_to_json_file(my_obj, filename):
    """definition of function """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
