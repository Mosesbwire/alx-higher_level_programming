#!/usr/bin/python3
"""
Module 2-append_write

"""


def append_write(filename="", text=""):
    """ Appends data to a file
        Args:
            filename (str): name of file
            text (data): data to write to file
        Returns: number of characters written to file
    """

    data = str(text)
    num_of_chars = 0

    if len(filename) == 0:
        filename = "file_01"

    with open(filename, "a", encoding="utf-8") as f:
        num_of_chars = f.write(data)

    return num_of_chars
