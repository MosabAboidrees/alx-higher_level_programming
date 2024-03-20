#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update or add the key/value pair in the dictionary.
    # If the key exists, its value is updated.
    # If the key does not exist, the key/value pair is added.
    a_dictionary[key] = value
    # Return the updated dictionary.
    return a_dictionary
