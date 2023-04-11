#!/usr/bin/python3
"""
module 3-is_kind_of_class

has method that checks if object is an instance of

"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of a class or instance of class that
    class has inherited from
    Args:
        obj (object): argument to check if is instance of @a_class
        a_class (class): argument to comapre @obj against
    Returns:
        True if obj is instance of a_class or parent of a_class
        otherwise False
    """
    return isinstance(obj, a_class)
