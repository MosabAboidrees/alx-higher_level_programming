#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Creates a copy of the string without the character at position n.
    :param str: The original string.
    :param n: The index of the character to remove.
    :return: A new string with the character at index n removed.
    """
    # Check if the index is out of the valid range
    if n < 0 or n >= len(str):
        return str

    # Build the new string without the character at index n
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    
    return new_str
