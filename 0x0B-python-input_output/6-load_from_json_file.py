#!/usr/bin/python3
"""function that creates an Object from a 'JSON(filename)': """
import json


def load_from_json_file(filename):
    """definition of function """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
