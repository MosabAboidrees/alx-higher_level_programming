#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuples to at least 2 elements, using 0 if they are shorter
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Calculate the sum of the first two elements of each tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
