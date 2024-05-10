#!/usr/bin/python3
"""
This module contains a function that formats text by inserting two new lines
after each '.', '?', or ':', and removes spaces at the beginning or end of
each resulting line.
"""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', or ':'.
    Leading and trailing spaces around these punctuation marks are removed.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If the input is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Create a copy of the input text to avoid modifying the original string
    formatted_text = text[:]

    # Iterate through each punctuation mark
    # that should be followed by new lines
    for delimiter in ".?:":  # Delimiters to check
        # Split the text by the current
        # delimiter and strip spaces around splits\
        segments = formatted_text.split(delimiter)
        formatted_text = ""
        for segment in segments:
            segment = segment.strip(" ")
            # Check if the formatted_text is empty
            if formatted_text == "":
                # If formatted_text is empty,
                # simply add the current segment and delimiter
                formatted_text = segment + delimiter
            else:
                # If formatted_text is not empty, append two new lines,
                # the segment, and the delimiter
                formatted_text += "\n\n" + segment + delimiter

    # Print the final formatted text, slicing off the
    # extra new lines added at the end
    print(formatted_text[:-3], end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
