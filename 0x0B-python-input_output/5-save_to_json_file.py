#!/usr/bin/python3
"""
Module 5-save_json_to_file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes a serialized python object to a file
    Args:
        my_obj (object): object to serialize and write to file
        filename (str): name of file to write to
    """
    if len(filename) == 0:
        filename = "file_01"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
