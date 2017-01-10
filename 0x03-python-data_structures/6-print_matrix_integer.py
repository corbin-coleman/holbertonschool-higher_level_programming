#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    index = 0
    for i in matrix:
        for j in matrix[index]:
            print("{:d}".format(j), end="")
            if j != matrix[index][-1]:
                print(" ", end="")
        print("")
        index += 1
