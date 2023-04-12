#!/usr/bin/python3
"""
Module 11-student
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

    def to_json(self, attrs=None):
        """return instance __dict__ with simple data types """
        if attrs is None:
            return self.__dict__
        new_dict = {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return new_dict

    def reload_from_json(self, json):
        """ sets attribute values from json """
        for key, value in json.items():
            setattr(self, key, value)
