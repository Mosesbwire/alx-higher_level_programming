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
        try:
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size
