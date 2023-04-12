#!/usr/bin/python3
"""
Module 4-from_json_string

"""
import json


def from_json_string(my_str):
    """ deserializes a JSON string
    Args:
        my_str (json string): string to deserialize
    Returns: a Python object
    """
    return json.loads(my_str)
