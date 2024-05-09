#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            # Convert to uppercase by subtracting 32 from ASCII value
            temp = ord(char) - 32
        else:
            # Print non-lowercase characters as they are
            temp = ord(char)
        print("{:c}".format(ord(temp)), end='')
    print()  # Print a new line at the end of the string
