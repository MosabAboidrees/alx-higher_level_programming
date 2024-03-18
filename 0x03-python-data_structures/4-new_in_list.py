#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Copy the list using list slicing
    new_list = my_list[:]
    # Check if index is within the valid range
    if 0 <= idx < len(new_list):
        # Replace the element at the specified index
        new_list[idx] = element
    # Return the modified copy of the list
    return new_list
