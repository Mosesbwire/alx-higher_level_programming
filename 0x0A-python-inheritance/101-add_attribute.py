#!/usr/bin/python3
"""
module 101-add_attribute

sets attribute of an object

"""


def add_attribute(obj, key, value):
    """dynamically set the attribute of an object
    Args:
        obj (object): object to set value
        key (str): name of the attribute
        value (obj): value for the attribute
    """
    if (type(obj) in (int, float, complex, str, tuple, frozenset)
            or hasattr(obj,"__slots__")):
        raise TypeError("can\'t add new attribute")
    setattr(obj, key, value)
