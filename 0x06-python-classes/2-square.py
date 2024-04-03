#!/usr/bin/python3

class Square:
    """Defines a square by its size, with validation."""

    def __init__(self, size=0):
        """Initializes the square with a size.

        Args:
            size (int): The size of the square, with a default value of 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size