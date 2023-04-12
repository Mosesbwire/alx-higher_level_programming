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
        Raises:
            TypeError: if first or last name is not string or age is not int
            ValueError: if age is < 0
        """

        if (type(first_name) is not str):
            raise TypeError("first_name must be a string")
        if (type(last_name) is not str):
            raise TypeError("last_name must be a string")
        if (len(first_name) == 0 or len(last_name) == 0):
            raise TypeError("first_name or last name cannot be empty string")

        if (type(age) is not int):
            raise TypeError("age must be an int")
        if (age < 0):
            raise ValueError("age cannot be less than 0")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return instance __dict__ with simple data types """
        class_dict = self.__dict__
        new_dict = {key: value for key, value in class_dict.items()
                    if type(value) in (int, list, dict, bool, str)}
        return new_dict
