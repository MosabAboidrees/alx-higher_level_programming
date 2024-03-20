#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a list of keys to be deleted
    # to avoid modifying the dictionary
    # during iteration, which can lead to a runtime error.
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    # Iterate over the list of keys to delete
    # and remove each one from the dictionary.
    for key in keys_to_delete:
        del a_dictionary[key]
    # Return the modified dictionary after
    # removing all keys with the given value.
    return a_dictionary
