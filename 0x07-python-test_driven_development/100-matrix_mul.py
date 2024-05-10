def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the result.

    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats.
        ValueError: If m_a or m_b is empty or cannot be multiplied due to size.

    Returns:
        list: Matrix resulting from the multiplication of m_a and m_b.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or \
       not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if m_a == [] or m_b == [] or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or \
       not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a and m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or \
       not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a and m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(sum_product)
        result.append(row)
    return result
