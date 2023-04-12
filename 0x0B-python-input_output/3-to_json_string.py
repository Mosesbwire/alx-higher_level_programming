#!/usr/bin/python3
"""
Module 3-to_json_string

"""
import json


def to_json_string(my_obj):
    """ serializes an object
    Args:
        my_obj (object): object to serialize with json
    Returns: serialized object
    """
    return json.dumps(my_obj)
