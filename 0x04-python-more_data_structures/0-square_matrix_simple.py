#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use a list comprehension to iterate through rows and then each element in the row
    # Square each element and construct the new row, and then construct the new matrix
    return [[x**2 for x in row] for row in matrix]
