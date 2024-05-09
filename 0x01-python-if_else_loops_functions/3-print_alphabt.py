#!/usr/bin/python3
for char in range(97, 123):  # ASCII values for 'a' to 'z'
    if chr(char) != 'q' and chr(char) != 'e':
        print("{}".format(chr(char)), end='')
