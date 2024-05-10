#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100.
    For multiples of three, print 'Fizz' instead of the number.
    For multiples of five, print 'Buzz.'
    For numbers multiples of three and five, print 'FizzBuzz.'
    Each element is followed by a space except for the last element.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end='')
        elif i % 3 == 0:
            print("Fizz", end='')
        elif i % 5 == 0:
            print("Buzz", end='')
        else:
            print(i, end='')
        print(" ", end='')
