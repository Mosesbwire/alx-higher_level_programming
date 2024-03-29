#!/usr/bin/python3
"""
Module 2-square
Defines a square
"""


class Square:
    """ Represents a square """

    def __init__(self, size=0):
        """
        initializes the object
        Args:
            size (int): length of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
