#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda n: n ** 2, row)), matrix))
    """ function that computes the square value of all integers of a
    matrix using map """
