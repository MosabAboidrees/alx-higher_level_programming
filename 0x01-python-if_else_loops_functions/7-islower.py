def islower(c):
    """
    Check if a character is a lowercase letter.
    
    :param c: Character to check
    :return: True if c is lowercase, False otherwise
    """
    return 97 <= ord(c) <= 122  # 'a' to 'z' in ASCII
