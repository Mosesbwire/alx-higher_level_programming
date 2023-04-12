#!/usr/bin/python3
"""
Module 9-student
Gets simple data structures from object __dict__
"""


class Student:
    """Represents a student object
    """

    def __init__(self, first_name, last_name, age):
        """initializes a student object
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return instance __dict__ with simple data types """
        return self.__dict__
