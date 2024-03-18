#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char not in ['c', 'C']:
            new_string += char
    return new_string
# or we can use this method
# return ''.join(char for char in my_string if char not in ['c', 'C'])
