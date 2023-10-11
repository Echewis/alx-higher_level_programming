#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
    """ This fuction will delete a key with its value from the dictionary
    if the value imputed does not exist in the dictionary, nothing will happen
    """
