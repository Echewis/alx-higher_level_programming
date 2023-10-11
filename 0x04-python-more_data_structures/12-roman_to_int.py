#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    former_num = 0
    for char in roman_string:
        value = roman_d.get(char, 0)
        if value == 0:
            return (0)
        if value > former_num:
            output += value - 2 * former_num
        else:
            output += value
        former_num = value
    return (output)
    """ Function that converts Roman to integer """
