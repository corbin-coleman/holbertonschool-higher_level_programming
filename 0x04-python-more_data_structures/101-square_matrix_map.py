#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda sublist: list(map(lambda val: val ** 2, sublist)), matrix))]
