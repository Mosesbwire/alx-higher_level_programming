#!/usr/bin/python3
"""
Module prints a square

"""


def print_square(size):

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
        return

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    print_square(5)
