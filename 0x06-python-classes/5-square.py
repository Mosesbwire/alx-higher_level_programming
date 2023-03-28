#!/usr/bin/python3
"""
Module 5-square
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
        self.__size = size

    def area(self):
        """calculates area of a square.
        Returns: Area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ getter returns the private instance variale size
            setter checks if value is an integer
            setter throws TypeError if value is not int
            setter throws ValueError if value is < 0
        """
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints a square
            prints an emptyl line if size is zero
        """
        if self.size == 0:
            print()

        for i in range(self.size):
            for x in range(self.size):
                print("#", end="")
            print()
