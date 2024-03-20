#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is not a string or if it's None, then return 0.
    if not isinstance(roman_string, str):
        return 0
    
    # Dictionary to map Roman numerals to their integer values.
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize integer to store the total value.
    integer_value = 0
    
    # Loop through each character in the Roman numeral string.
    for i in range(len(roman_string)):
        # If this is the last character, or if the current numeral is equal to
        # or greater than the numeral following it, add its value.
        if i == len(roman_string) - 1 or roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            integer_value += roman_dict[roman_string[i]]
        # Otherwise, subtract its value (for cases like IV, IX, etc.).
        else:
            integer_value -= roman_dict[roman_string[i]]
    
    # Return the total value as an integer.
    return integer_value
