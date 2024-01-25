#!/usr/bin/python3
"""
peak in an unsorted int
"""


def find_peak(list_of_integers):
    """
    Args:
        list of intgers: is the list of integers
    Returns: will return peak of list_of_integers or nothing
    """
    size = len(list_of_integers)
    mi = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mi = mi // 2
        if (mid < size - 1 and list_of_integers[mid]
                < list_of_integers[mid + 1]):
            if mi // 2 == 0:
                mi = 2
            mid = mid + mi // 2
        elif mi > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mi // 2 == 0:
                mi = 2
            mid = mid - mi // 2
        else:
            return list_of_integers[mid]
