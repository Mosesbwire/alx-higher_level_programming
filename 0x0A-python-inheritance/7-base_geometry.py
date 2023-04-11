#!/usr/bin/python3

"""
Module 7-base_geometry

Has class BaseGeometry
"""


class BaseGeometry():
    """Empty base class """

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates that value is an integer

        Args:
            name (str): name of value being checked
            value (int): argument being checked if is integer
        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
