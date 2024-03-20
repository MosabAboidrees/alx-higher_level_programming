#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Attempt to delete the key from the dictionary.
    # The pop method removes the item with the provided key and returns its value.
    # If the key doesn't exist, it returns the default value, here None,
    # and does not raise a KeyError.
    a_dictionary.pop(key, None)
    # Return the (potentially) updated dictionary.
    return a_dictionary
