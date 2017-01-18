#!/usr/bin/python3
"""
This is the ``Matrix`` module

Contains the function ``matrix_divided`` which divides a matrix of ints/floats
by a given int
"""
def matrix_divided(matrix, div):
    """
    Return a new_matrix of all items in matrix divided by div, all items in
    new_matrix should be floats rounde to 2 decimal points max
    """
    lengths = []
    new_matrix = []
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        quotients = []
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for x in i:
            if type(x) != int and type(x) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            quotients.append(round(x / div, 2))
        length = len(i)
        if length not in lengths:
            lengths.append(length)
        new_matrix.append(quotients)
    if len(lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
