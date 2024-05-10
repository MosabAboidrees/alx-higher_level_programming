#!/usr/bin/python3
"""
This module contains a function that indents text after each punctuation mark
specified (.?;), with two new lines and removes any spaces at the beginning
or at the end of the new line.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ".?:":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
