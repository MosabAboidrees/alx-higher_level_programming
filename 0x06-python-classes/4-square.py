#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square by its size,
    with validation, calculates its area,
    and allows size manipulation."""

    def __init__(self, size=0):
        """Constructor.
        Initializes the square with a size.

        Args:
            size: The size of the square,
            with a default value of 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size ** 2
