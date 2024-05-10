#!/usr/bin/python3
"""
This module multiplies 2 matrices using the module NumPy.

Functions:
- lazy_matrix_mul(m_a, m_b): Multiplies two matrices
using NumPy's matmul function.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The result of multiplying the two matrices.

    """
    return (np.matmul(m_a, m_b))
