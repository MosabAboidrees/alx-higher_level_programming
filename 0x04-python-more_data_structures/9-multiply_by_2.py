#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Use a dictionary comprehension to iterate over each item in the original
    # dictionary. For each item, the key is kept the same, and the value is
    # multiplied by 2. The result is a new dictionary where all values are
    # doubled.
    return {key: value * 2 for key, value in a_dictionary.items()}
