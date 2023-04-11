#!/usr/bin/python3

"""
Module 4-inherits_from

Has function to check if an object is a subclass of given class

"""


def inherits_from(obj, a_class):
    """ checks if obj is an instance of a_class directly or indirectly
    Args:
        obj (object): object to check if is instance of a_class
        a_class (class): class to compare obj against
    Returns:
        True if obj inherits from a_class
        otherwise False
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
