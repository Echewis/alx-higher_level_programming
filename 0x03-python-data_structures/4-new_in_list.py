#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    photocopy = [i for i in my_list]
    photocopy[idx] = element
    return (photocopy)
    """ this function will copy and replace item in the list but
    changes will happen on the copied list"""
