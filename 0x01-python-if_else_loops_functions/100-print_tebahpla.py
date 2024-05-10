#!/usr/bin/python3
for i in range(26):
    # Calculate the ASCII value for the letter to print
    # Start from 'z' (122) and 'Y' (89), decrement by 2
    # for lowercase and by 2 for uppercase alternatively
    print("{:c}".format(122 - i if i % 2 == 0 else 89 - i), end='')
