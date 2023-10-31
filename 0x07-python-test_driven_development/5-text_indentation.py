#!/usr/bin/python3
"""

This module contains function idents line

"""


def text_indentation(text):
    """definition of function


    parameters:
        text: input string

    Returns:
        nothing

    Raises:
        TypeError: if text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    t = text[:]

    for q in ".?:":
        ord_text = t.split(q)
        t = ""
        for o in ord_text:
            o = o.strip(" ")
            t = o + q if t is "" else t + "\n\n" + o + q

    print(t[:-3], end="")
