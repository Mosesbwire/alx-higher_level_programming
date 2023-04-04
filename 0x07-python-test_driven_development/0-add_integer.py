#!/usr/bin/python3
"""Adds numbers """


def add_integer(a, b=98):
    """
    Floats are casted to ints
    Returns sum of two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    print(add_integer(10, 20))
