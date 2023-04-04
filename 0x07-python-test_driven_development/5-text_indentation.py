#!/usr/bin/python3

"""
Prints a formatted text.
Add a newline after each . ? :

"""

def text_indentation(text):
    """ prints text replacing . ? : with a newline
    Args:
        text (string): string to be formatted and printed
    Raises:
        TypeError: if text is not string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
