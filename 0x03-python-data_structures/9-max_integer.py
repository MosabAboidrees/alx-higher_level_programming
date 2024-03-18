#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None
    my_list.sort()  # Sorts the list in place
    return my_list[-1]  # Returns the last element
