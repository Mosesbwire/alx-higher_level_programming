#!/usr/bin/python3

"""
Module for the base class

"""
import json


class Base:
    """ this is the base class for this project. It manages the id attribute
    for all classes that inherit from it

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor
        Args:
            id (int): id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """ creates an instance of cls"""
        if cls.__name__ == 'Rectangle':
            placeholder = cls(1, 1)
        elif cls.__name__ == 'Square':
            placeholder = cls(10)
        else:
            raise TypeError('invalid class')
        placeholder.update(**dictionary)
        return placeholder
