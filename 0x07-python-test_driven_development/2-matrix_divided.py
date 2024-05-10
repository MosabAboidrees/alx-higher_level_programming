#!/usr/bin/python3
"""
This module provides a function that divides all elements
in a matrix by a given divisor.
"""

def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by div,
    rounding the result to 2 decimal places.

    Args:
        matrix (list of list of int/float): Matrix to be divided.
        div (int/float): Number by which matrix elements will be divided.

    Returns:
        list of list of float: New matrix with
        each element divided by the divisor.

    Raises:
        TypeError: If matrix elements are not lists of integers or floats,
                   if any element in these lists is not an integer or float,
                   if div is not a number, or if rows of the matrix
                   are not the same size.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")  # Adjusted the error message to match the expected output

    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    if len(matrix) == 0:
        raise TypeError(error_msg)

    row_length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list) or not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(error_msg)
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Using list comprehension for clarity and conciseness
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
