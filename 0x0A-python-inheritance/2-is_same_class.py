#!/usr/bin/python3

"""
Module 2-is_same_class

constains method that checks if an object is an instance of a given class

"""


def is_same_class(obj, a_class):
    """checks that a @obj is an instance of @a_class
    Args:
        obj (object): argument to compare to @a_class
        a_class (class): argument to compare @obj against
    Returns:
        True if @obj is instance of @a_class
        otherwise False
    """
    return type(obj) == a_class
