#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the symmetric difference operator '^' to find elements
    # that are in either set_1 or set_2 but not in both.
    return set_1 ^ set_2
