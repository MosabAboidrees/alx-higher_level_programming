#!/usr/bin/python3

"""

This module contains a function that multiplies two matrices.

The function performs various validations to ensure the matrices are compatible
for multiplication. It checks if the matrices are:

* Lists
* Lists of lists
* Contain only integers or floats
* Have rows of the same size (for each matrix individually)
* Have compatible dimensions for multiplication (number of columns in the first
  matrix must equal the number of rows in the second matrix)

If any of these validations fail, a specific TypeError or ValueError is raised.

"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices.

    Args:
        m_a (list of lists of int/float): The first matrix to be multiplied.
        m_b (list of lists of int/float): The second matrix to be multiplied.

    Raises:
        TypeError: If any of the following conditions are not met:
            * m_a or m_b is not a list.
            * m_a or m_b is not a list of lists.
            * An element in m_a or m_b is not an integer or float.
            * Rows in m_a or m_b are not of the same size.
        ValueError: If any of the following conditions are not met:
            * m_a or m_b is empty.
            * m_a and m_b cannot be multiplied due to incompatible dimensions

    Returns:
        A new list representing the result of the multiplication of m_a and m_b.

    """


    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if elements in m_a and m_b are integers or floats
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    # Check if all rows in m_a have the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    # Check if all rows in m_b have the same size
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    # Check if m_a and m_b have compatible dimensions for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Transpose m_b for efficient multiplication
    trans = []
    for col in range(len(m_b[0])):
        my_row = []
        for row in range(len(m_b)):
            my_row.append(m_b[row][col])
        trans.append(my_row)

    # Perform matrix multiplication
    tesult = []
    for row in m_a:
        my_row = []
        for column in trans:
            product = 0
            for m in range(len(trans[0])):
                product += row[m] * column[m]
            my_row.append(product)
        tesult.append(my_row)

    return tesult