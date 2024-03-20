#!/usr/bin/python3
def number_keys(a_dictionary):
    # The len() function is used to return the number of keys in the dictionary.
    # a_dictionary.keys() returns a view of the dictionary's keys.
    # Wrapping it with len() counts the number of items in this view.
    return len(a_dictionary.keys())
