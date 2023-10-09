#!/usr/bin/python3
""" This function will find numbers that can multiply by 2"""
def divisible_by_2(my_list=[]):
    divide = []
    for d in range(len(my_list)):
        if my_list[d] % 2 == 0:
            divide.append(True)
        else:
            divide.append(False)

    return (divide)
