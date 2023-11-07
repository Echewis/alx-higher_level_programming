#!/usr/bin/python3
"""This is a script that adds all argument to a Python list
and then save them to a file
"""
import json
import sys
from typing import List


def save_to_json_file(my_obj, filename):
    """definition of funtion save_to_json_file """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """definition of function """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))


def add_to_list_and_save(args: List[str], filename: str):
    """Function that adds to list and save """
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_to_list_and_save(args, "add_item.json")
