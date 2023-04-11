#!/usr/bin/python3
"""
Module 100-my_int

Inverses the == and != operators

"""


class MyInt(int):
    """ Extends the int class """

    def __init__(self, my_int):
        """initializes object """
        self.__my_int = my_int

    def __eq__(self, value):
        if self.__my_int == value:
            return False
        return True

    def __ne__(self, value):
        if self.__my_int == value:
            return True
        return False
