#!/usr/bin/python3

"""
Returns the methods and attributes available in an object as a list

"""


def lookup(obj):
    """ returns available attributes and methods in @obj
    Args:
        obj (object): object to get attributes and methods from

    Returns:
        A list of available attributes and methods found in @obj
    """
    attributes_list = list(object.__dict__.keys()) + list(obj.__dict__.keys())
    sorted_list = sorted(attributes_list)
    return sorted_list
