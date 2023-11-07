#!/usr/bin/python3
"""function that defines a text file insertion """


def append_after(filename="", search_string="", new_string=""):
    """function definition append """
    Text = ""
    with open(filename) as r:
        for Line in r:
            Text += Line
            if search_string in Line:
                Text += new_string
    with open(filename, "w", encoding="utf-8") as w:
        w.write(Text)
