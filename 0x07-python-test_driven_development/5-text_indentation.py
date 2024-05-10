#!/usr/bin/python3
"""
This module contains a function that processes text
by inserting two new lines after each '.', '?', or ':',
while removing spaces at the beginning or end of each line and
immediately following these punctuation marks.
"""


def text_indentation(text):
    """
    Processes the input text to add two new lines after
    '.', '?', and ':' punctuation marks and ensures there
    are no spaces at the beginning or end of each printed segment.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Strip leading and trailing whitespaces from the entire text first
    text = text.strip()

    i = 0
    start = 0  # Start index for each segment
    while i < len(text):
        # Print each character until a punctuation is found
        if text[i] in ".?:":
            # Print the segment up to and including the current character
            # Strip right side spaces from each segment before the punctuation
            print(text[start:i+1].rstrip())
            print()  # Print the two new lines
            start = i + 1  # Update start to the character after punctuation
            # Skip any spaces immediately after the punctuation
            while start < len(text) and text[start] == ' ':
                start += 1
            i = start - 1  # Reset i to continue from the new start position
        i += 1

    # If there's any remaining text after the last punctuation, print it
    if start < len(text):
        print(text[start:].rstrip())  # Ensure to strip trailing spaces


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
