#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase by subtracting 32 from ASCII value
        else:
            result += char  # Include non-lowercase characters as they are
    print(result)
