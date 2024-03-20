#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Define a function that squares all elements in a row
    def square_row(row):
        return list(map(lambda x: x**2, row))
    
    # Use map to apply square_row to each row in the matrix and convert the result to a list
    return list(map(square_row, matrix))