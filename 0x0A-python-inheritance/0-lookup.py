#!/usr/bin/python3

"""
Module 0-lookup

contains method lookup that returns a list of available attributes and methods
in an object

"""


def lookup(obj):
    """ returns available attributes and methods in @obj
    Args:
        obj (object): object to get attributes and methods from

    Returns:
        A list of available attributes and methods found in @obj
    """
    return dir(obj)
