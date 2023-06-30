#!/usr/bin/python3
"""
    Finds the peak value in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
        takes a list of integers and finds the peak
    """
    head = 0
    tail = len(list_of_integers) - 1
    peak = None
    curr_peak = None

    while head < tail:

        curr_peak = list_of_integers[head] if list_of_integers[head] >= list_of_integers[tail] else list_of_integers[tail]

        if peak is None:
            peak = curr_peak

        if curr_peak > peak:
            peak = curr_peak

        head += 1
        tail -= 1
    return peak
