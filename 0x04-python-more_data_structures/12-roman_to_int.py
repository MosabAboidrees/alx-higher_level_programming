#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is not a string; return 0 for invalid input.
    if not isinstance(roman_string, str):
        return 0
    # Initialize total to accumulate the numerical value.
    total_value = 0
    # Initialize num to keep track of the numeric value of the current Roman numeral.
    current_roman_value = 0
    # A dictionary mapping each Roman numeral character to its integer value.
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Iterate through the Roman numeral string in reverse order.
    for idx in reversed(roman_string):
        # Get the integer value of the current Roman numeral character.
        current_roman_value = roman_dict[idx]
        # Add the value of the current numeral to the total if the total so far is less
        # than 5 times the current numeral's value. Otherwise, subtract it.
        # This handles the Roman numeral subtraction rule (e.g., IV is 4, IX is 9).
        if total_value < current_roman_value * 5:
            total_value += current_roman_value
        else:
            total_value -= current_roman_value
    # Return the total calculated value.
    return total_value
