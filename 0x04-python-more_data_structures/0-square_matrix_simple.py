#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_row = []
        for j in range(0, len(i)):
            new_row.append(i[j] * i[j])
        new_matrix.append(new_row)

    return new_matrix
