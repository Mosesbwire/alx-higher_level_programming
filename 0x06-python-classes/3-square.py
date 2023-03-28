#!/usr/bin/python3
"""
Module 3-square
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

    def area(self):
        """calculates area of a square.
        Returns: Area of a square
        """
        return self.__size * self.__size
