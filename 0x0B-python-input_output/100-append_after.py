#!/usr/bin/python3
"""
Module 100-append_after
Searches for a string text in a file
Writes a new line after line with given srearch word is found

"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a new string to file in the next line where
    the search_string has been found
    Args:
        filename (str): name of file
        search_string (str): string to lookup
        new_string (str): string to append to file
    """
    new_data = []
    with open(filename, "r+", encoding="utf-8") as f:
        for line in f:
            new_data.append(line)
            if search_string in line:
                new_data.append(new_string)

        f.seek(0)
        f.writelines(new_data)
