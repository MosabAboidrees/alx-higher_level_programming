#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []  # Create a new matrix to store the squared values
    for row in matrix: # Iterate through the rows of the matrix
        new_matrix.append(list(map(lambda x: x**2, row))) # Square each element in the row and append to new_matrix
    return new_matrix  # Return the new matrix