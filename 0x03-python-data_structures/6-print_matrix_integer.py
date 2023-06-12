#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for a, j in enumerate(i):
            if a != len(i) - 1:
                print("{:d} ".format(j), end="")
            else:
                print("{:d}".format(j))
