#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square by its size,
    with validation, calculates its area,
    allows size manipulation, and prints the square."""

    def __init__(self, size=0):
        """Initializes the square with a size.

        Args:
            size: Length of a side of the square.
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
        """Returns the current square area.

        Returns:
            The size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character
        or an empty line if size is 0."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
