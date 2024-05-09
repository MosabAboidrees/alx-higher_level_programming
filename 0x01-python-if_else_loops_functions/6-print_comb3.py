#!/usr/bin/python3
for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        if first_digit != second_digit:  # Ensure the digits are different
            if second_digit == 9 and first_digit == 8:
                print("{:d}{:d}".format(first_digit, second_digit))
            else:
                print("{:d}{:d}".format(first_digit, second_digit), end=', ')
