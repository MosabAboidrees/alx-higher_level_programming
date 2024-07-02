# 0x08. Python - More Classes and Objects

This project is part of the ALX Higher Level Programming curriculum. It focuses on advanced concepts of object-oriented programming in Python, specifically working with classes and objects.

## Table of Contents

- [0. Simple rectangle](#0-simple-rectangle)
- [1. Real definition of a rectangle](#1-real-definition-of-a-rectangle)
- [2. Area and Perimeter](#2-area-and-perimeter)
- [3. String representation](#3-string-representation)
- [4. Eval is magic](#4-eval-is-magic)
- [5. Detect instance deletion](#5-detect-instance-deletion)
- [6. How many instances](#6-how-many-instances)
- [7. Change representation](#7-change-representation)
- [8. Compare rectangles](#8-compare-rectangles)
- [9. A square is a rectangle](#9-a-square-is-a-rectangle)
- [10. N queens](#10-n-queens)

## 0. Simple rectangle

Write an empty class `Rectangle` that defines a rectangle:

- You are not allowed to import any module

## 1. Real definition of a rectangle

Write a class `Rectangle` that defines a rectangle by:

- Private instance attribute: `width`
  - Property `def width(self):` to retrieve it
  - Property setter `def width(self, value):` to set it
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - If `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`
  - Property `def height(self):` to retrieve it
  - Property setter `def height(self, value):` to set it
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - If `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`

## 2. Area and Perimeter

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - If `width` or `height` is equal to 0, perimeter is equal to 0

## 3. String representation

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- `print()` and `str()` should print the rectangle with the character `#`:
  - If `width` or `height` is equal to 0, return an empty string

## 4. Eval is magic

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

## 5. Detect instance deletion

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted

## 6. How many instances

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- Public class attribute `number_of_instances`:
  - Initialized to 0
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion

## 7. Change representation

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- Public class attribute `print_symbol`:
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type

## 8. Compare rectangles

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  - Returns `rect_1` if both have the same area value

## 9. A square is a rectangle

Write a class `Rectangle` that defines a rectangle by:

- All previous task requirements
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`

## 10. N queens

Write a program that solves the N queens problem.

- Usage: `nqueens N`
  - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- Where `N` must be an integer greater or equal to `4`
  - If `N` is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
  - If `N` is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
  - One solution per line
  - Format: `[[r, c], [r, c], [r, c], [r, c], ...]`
  - You don’t have to print the solutions in a specific order

## Repository

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x08-python-more_classes`
