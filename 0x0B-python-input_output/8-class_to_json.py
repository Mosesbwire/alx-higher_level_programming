#!/usr/bin/python3
"""
Module 8-class_to_json
Serializes the attributes of class

"""


def class_to_json(obj):
    """ creates a class dict with only simple data structures int, dict, str
    bool and list
    Args:
        obj (instance of a class): instance to get dict
    Returns: a dict with simple data structures
    """
    class_dict = obj.__dict__
    new_dict = {key: value for key, value in class_dict.items()
                if type(value) in (list, int, dict, str, bool)}

    return new_dict
