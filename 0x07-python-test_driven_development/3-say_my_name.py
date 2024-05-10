#!/usr/bin/python3
"""
This module defines a function say_my_name which prints the full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name from the given first name and last name.
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print, optional.
    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
