#!/usr/bin/python3
"""
This module contains a function that indents text after each punctuation mark
specified (.?;), with two new lines and removes any spaces at the beginning
or at the end of the new line.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.
    There should be no space at the beginning or at the end
    of each printed line.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Strip the text first to remove leading and trailing spaces
    text = text.strip()

    i = 0
    start = 0  # Track the start of a segment of text
    while i < len(text):
        if text[i] in ".?:":
            # Print the segment up to this character,
            # strip to remove leading/trailing spaces
            print(text[start:i + 1].strip())
            print()  # Print the newline required by the task
            start = i + 1  # Move start to character after current punctuation
            # Skip any space after the punctuation before starting new line
            while start < len(text) and text[start] == ' ':
                start += 1
            i = start - 1  # Adjust i to continue from the new start
        i += 1

    # Print any remaining text after the last punctuation mark if there is any
    if start < len(text):
        print(text[start:].strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
