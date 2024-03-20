#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is not None and not empty
    if a_dictionary and len(a_dictionary) > 0:
        # Use max function with key argument to find the key with the maximum value
        return max(a_dictionary, key=a_dictionary.get)
    # If the dictionary is None or empty, return None
    return None
