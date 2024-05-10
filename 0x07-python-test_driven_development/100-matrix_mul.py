#!/usr/bin/python3
"""Module for matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Multiplies one matrix by another.
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the product
    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for num in row:  # check if the element is an int or a float
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):  # m_a columns must be equal to m_b rows
        raise ValueError("m_a and m_b can't be multiplied")

    # create a list of lists with the same length as m_a
    result = [[] for i in range(len(m_a))]

    for row in range(len(m_a)):  # rows of m_a
        for col in range(len(m_b[0])):  # columns of m_b
            # c is the sum of products of the row of m_a and the column of m_b
            c = 0
            for k in range(len(m_b)):
                c += m_a[row][k] * m_b[k][col]
            result[row].append(c)

    return result
