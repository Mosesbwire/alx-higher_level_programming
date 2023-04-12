#!/usr/bin/python3
"""
Module 1-write_file

"""


def write_file(filename="", text=""):
    data = str(text)
    num_of_chars = 0

    if len(filename) == 0:
        filename = "file_01"

    with open(filename, "w", encoding="utf-8") as f:
        num_of_chars = f.write(data)

    return num_of_chars
