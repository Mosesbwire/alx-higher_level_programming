#!/usr/bin/python3
"""
Module 10-square
Represents a square

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size):
        """ initializes square object """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates area"""
        return self.__size * self.__size
