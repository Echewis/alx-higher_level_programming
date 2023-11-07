#!/usr/bin/python3
"""This function will return JSON representation of an object(string)"""
import json


def to_json_string(my_obj):
    """definition of function to_json_string """
    return (json.dumps(my_obj))
