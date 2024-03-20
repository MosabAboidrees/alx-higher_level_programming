#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Iterate over the sorted keys of the dictionary.
    # The sorted() function returns a list of all the keys in the dictionary,
    # sorted in alphabetical order.
    for key in sorted(a_dictionary.keys()):
        # Print each key and its corresponding value.
        # The format is key: value, where key is a string (as we can assume
        # all keys are strings according to the task requirements) and value
        # can be of any type.
        print("{}: {}".format(key, a_dictionary[key]))
