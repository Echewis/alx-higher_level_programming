#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for n in range(len(my_list)):
        print("{:d}".format(my_list[n]))
    """ another way is
    for n in my_list:
        if isinstance(n, int):
        print("{}".format(n))
        """
