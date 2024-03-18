#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i < len(row) - 1:  # If not the last element, add a space
                print(" ", end="")
        print()  # Newline after each row
