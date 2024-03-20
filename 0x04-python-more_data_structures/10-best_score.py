#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is None.
    if a_dictionary is None:
        return None
    best_value = 0 # Assume the first key has the largest value.
    best_key = None # The key associated with the largest value.
    # Iterate over the keys in the dictionary.
    for key, value  in a_dictionary.items():
        # If the current key's value is greater than the largest known value,
        # update big_value and big_key to these new maximums.
        if value > best_value:
            best_value = value
            best_key = key
    # Return the key associated with the largest value.
    return best_key
