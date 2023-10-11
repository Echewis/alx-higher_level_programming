#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    final = []
    for row in matrix:
        fresh_row = []
        for material in row:
            fresh_row.append(material ** 2)
        final.append(fresh_row)
    return (final)
    """ This function will print the square of a variable
    """
