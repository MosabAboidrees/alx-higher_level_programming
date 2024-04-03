#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a square with size, position,
    and the ability to print itself to stdout."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, with validation."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character."""
        print(self.__str__())

    def __str__(self):
        """Return the string representation of the square,
        as it would be printed."""
        if self.__size == 0:
            return ""
        else:
            rows = []
            for _ in range(self.__position[1]):
                rows.append("")  # Add empty lines for the vertical position
            for _ in range(self.__size):
                rows.append(" " * self.__position[0] + "#" * self.__size)
            return "\n".join(rows)
