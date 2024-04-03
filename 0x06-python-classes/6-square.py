#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a square by its size and position,
    with validation, calculates its area,
    and prints the square considering its position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a size and a position.
        Args:
            size (int): The size of the square, with a default value of 0.
            position (int, int): The position of the square,
            with a default value of (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""

        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #, considering its position."""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
