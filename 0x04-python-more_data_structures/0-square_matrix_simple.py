#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for combs in matrix:
        new_matrix.append(list(map(lambda item: item * item, combs)))
    return new_matrix
