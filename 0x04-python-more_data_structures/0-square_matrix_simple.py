#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(x):
        return x**2
    new_matrix = matrix.copy()
    for i, x in enumerate(matrix):
        new_matrix[i] = list(map(square, x))

    return new_matrix
