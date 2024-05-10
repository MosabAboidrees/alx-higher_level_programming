#!/usr/bin/python3
"""
This module provides a function that divides all elements
in a matrix by a given divisor.
"""

def matrix_divided(matrix, div):
    """ 
    Divides each element of a matrix by a div,
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
                   if the divisor is not a number, or if rows of the matrix
                   are not the same size.
        ZeroDivisionError: If the divisor is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("divisor must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_msg)

    row_length = 0
    error_msg_size = "Each row of the matrix must have the same size"

    for element in matrix:
        if not element or not isinstance(element, list):
            raise TypeError(error_msg)

        if row_length is not None and len(element) != row_length:
            raise TypeError(error_msg_size)

        for num in element:
            if not type(num) in (int, float):
                raise TypeError(error_msg)

        row_length = len(element)

    # Using list comprehension for clarity and conciseness
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return m
