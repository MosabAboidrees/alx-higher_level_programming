#!/usr/bin/python3
"""
This module contains a function that processes text
by inserting two new lines after
each '.', '?', or ':', and ensures there are no trailing or
leading spaces around these punctuation marks.
"""


def text_indentation(text):
    """
    Processes the input text to add two new lines after
    '.', '?', and ':' punctuation marks.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove spaces after punctuation before adding two new lines
    punctuations = ".?:"
    i = 0
    while i < len(text):
        char = text[i]
        print(char, end='')
        if char in punctuations:
            print("\n")
            # Move the index forward and skip all spaces
            # until non-space or end of text
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
