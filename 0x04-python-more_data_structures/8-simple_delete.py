#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary.
    # The .get() method returns None if the key does not exist,
    # which prevents a KeyError if we were to use del without checking.
    if a_dictionary.get(key) is not None:
        # If the key exists, delete it from the dictionary.
        del a_dictionary[key]
    # Return the dictionary, which might have been modified
    # if the key existed and was successfully deleted.
    return a_dictionary
