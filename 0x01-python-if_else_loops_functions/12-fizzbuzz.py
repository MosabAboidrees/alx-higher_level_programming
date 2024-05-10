#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100.
    For multiples of three, prints 'Fizz' instead of the number.
    For multiples of five, prints 'Buzz'.
    For numbers multiples of three and five, print 'FizzBuzz.'
    Each element is followed by a space except for the last element.
    """
    result = []  # Using a list to store results for precise space control
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(" ".join(result))  # Join all elements with a space and print once
