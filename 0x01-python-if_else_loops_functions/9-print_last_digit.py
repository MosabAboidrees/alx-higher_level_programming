#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number and returns it.
    :param number: Integer whose last digit is to be printed
    :return: The last digit of the number
    """
    last_digit = abs(number) % 10  # Handle negative numbers correctly
    print(last_digit, end='')  # Print the last digit, stay on the same line
    return last_digit
