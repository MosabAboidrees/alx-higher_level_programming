#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty or None. If so, return None.
    if a_dictionary == {} or a_dictionary is None:
        return None
    # Convert dictionary keys to a list and initialize variables
    # to track the largest value and corresponding key.
    keys = list(a_dictionary)
    best_value = a_dictionary[keys[0]]  # Assume the first key has the largest value.
    best_key = keys[0]  # The key associated with the largest value.
    # Iterate over the keys in the dictionary.
    for key in keys:
        # If the current key's value is greater than the largest known value,
        # update big_value and big_key to these new maximums.
        if a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key
    # Return the key associated with the largest value.
    return best_key
