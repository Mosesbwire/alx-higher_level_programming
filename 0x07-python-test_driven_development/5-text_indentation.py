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

    for char in text:
        if (char == '.' or char == ':' or char == '?'):
            print()
            print()
        else:
            print(char, end="")
    if text[len(text) - 1] != '.' or text[len(text) - 1] != ':' or text[len(text) - 1] != '?':
        print()
        print()


if __name__ == "__main__":
    text_indentation("This string.Has all the charactrers? The list is: period, color")
