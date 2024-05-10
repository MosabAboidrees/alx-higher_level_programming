#!/usr/bin/python3
for i in range(25, -1, -1):
    # Calculate the ASCII value starting from 'A' and
    # adjusting for cases based on index
    char = i + ord('A')
    if i % 2 == 1:
        char += 32  # Make lowercase if the index is odd
    print("{:c}".format(char), end="")
