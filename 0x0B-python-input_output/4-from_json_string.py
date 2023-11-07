#!/usr/bin/python3
""" This function that return an object(python data structure)"""
import json


def from_json_string(my_str):
    """ definition of function from_json_string """
    return (json.loads(my_str))
