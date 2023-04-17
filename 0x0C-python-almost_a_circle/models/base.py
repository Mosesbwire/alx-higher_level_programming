#!/usr/bin/python3

"""
Module for the base class

"""


class Base:
    """ this is the base class for this project. It manages the id attribute
    for all classes that inherit from it

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor
        Args:
            id (int): id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
