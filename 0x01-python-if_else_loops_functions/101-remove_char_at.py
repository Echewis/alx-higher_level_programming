#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1:])
    """ this code will copy a string without the one in n position"""
