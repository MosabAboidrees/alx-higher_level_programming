#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Alx."""

import math


class MagicClass:
    """A class that represents a circle
    and allows calculation of its area and circumference.

    Attributes:
        __radius (float): The radius of the circle. Private attribute.
    Methods:
        __init__(self, radius=0): Initializes the MagicClass with a radius.
        area(self): Returns the area of the circle.
        circumference(self): Returns the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize the MagicClass with a specified radius.

        Validates the radius to ensure it is a number (int or float).
        If the radius is not a valid number, a TypeError is raised.

        Args:
            radius (int, float, optional): The radius of the circle.
            Defaults to 0.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        Uses the formula: area = πr²
        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculate and return the circumference of the circle.
        Uses the formula: circumference = 2πr
        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
