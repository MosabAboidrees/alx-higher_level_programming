#!/usr/bin/python3
"""
This module defines the print_square function that prints
a square of the character '#'.
"""


def print_square(size):
    """
    Prints a square with the character '#' based on the size provided.
    Args:
        size (int): The size length of the square's sides. Must be an
        integer greater than or equal to zero.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0, with a specific
        message indicating size must be an integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
