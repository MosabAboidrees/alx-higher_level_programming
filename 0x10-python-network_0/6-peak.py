#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    Args:
        list_of_integers (list of int):
        List of integers to find the peak of.
    Returns:
        int: A peak element of list_of_integers
        or None if the list is empty.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    low, high = 0, n - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
