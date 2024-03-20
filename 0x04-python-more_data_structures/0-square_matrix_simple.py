#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # return a new matrix with the square of each element
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix)) 