#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10  # Assign the value 10 to variable 'a'
    b = 5   # Assign the value 5 to variable 'b'
    # Perform operations using the imported functions and print the results.
    # The use of print function is minimized as per the requirement.
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
