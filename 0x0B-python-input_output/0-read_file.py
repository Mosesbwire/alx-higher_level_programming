#!/usr/bin/python3
"""
Module 0-read_file
Reads and prints data from file

"""


def read_file(filename=""):
    """ reads and prints data from given file
    Args:
        filename (str): name of file
    Raises:
        TypeError: if filename is not a string
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
