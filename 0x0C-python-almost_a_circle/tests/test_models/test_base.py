#!/usr/bin/python3
"""
this is the test module for the Base class

"""
import unittest
import os
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def setUp(self):
        """ create instances of Rectangle and Square to be used """
        self.rectangles = [
            Rectangle(20, 20, 20, 20, 20), Rectangle(10, 10, 10, 10, 10)]
        self.squares = [Square(5, 5, 5, 5), Square(3, 3, 3, 3)]
        Base._Base__nb_objects = 0

    def test_id(self):
        """ test initialization of id with default value """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        """ test initialization of id with custom value """
        b2 = Base(5)
        self.assertEqual(b2.id, 5)

        """ test increment of id with multiple instances """
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

        """ test setting id directly """
        b5 = Base()
        b5.id = 10
        self.assertEqual(b5.id, 10)

    def test_to_json_string(self):
        """ test conversion of empty list to JSON string """
        self.assertEqual(Base.to_json_string([]), "[]")

        """ test conversion of list of dictionaries to JSON string """
        my_list = [{'id': 1, 'x': 2, 'y': 3}, {'id': 2, 'x': 4, 'y': 5}]
        expected = '[{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]'
        self.assertEqual(Base.to_json_string(my_list), expected)

        """ test conversion of None to JSON string """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """ test conversion of empty string to empty list """
        self.assertEqual(Base.from_json_string(""), [])

        """ test conversion of JSON string to list of dictionaries """
        s = '[{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]'
        expected = [{'id': 1, 'x': 2, 'y': 3}, {'id': 2, 'x': 4, 'y': 5}]
        self.assertEqual(Base.from_json_string(s), expected)

        """ test conversion of None to empty list """
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file_rectangles(self):
        """Test saving a list of Rectangle instances to a file """
        Rectangle.save_to_file(self.rectangles)
        with open("Rectangle.json", "r") as file:
            contents = json.load(file)
            expected = [{"id": 20, "width": 20,
                         "height": 20, "x": 20, "y": 20}, {
                "id": 10, "width": 10, "height": 10, "x": 10, "y": 10}]
            self.assertEqual(contents, expected)

    def test_save_to_file_squares(self):
        """ Test saving a list of Square instances to a file """
        Square.save_to_file(self.squares)
        with open("Square.json", "r") as file:
            contents = json.load(file)
            expected = [{"id": 5, "size": 5, "x": 5, "y": 5},
                        {"id": 3, "size": 3, "x": 3, "y": 3}]
            self.assertEqual(contents, expected)

    def test_saving_empty_list(self):
        """ test saving emtpy list to file """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")

    def test_create_rectangle(self):
        """ tests the create function
            test by creating rectangles
        """
        r = Rectangle(1, 1)
        r_dict = r.to_dictionary()
        r_copy = Rectangle.create(**r_dict)
        self.assertIsInstance(r_copy, Rectangle)
        self.assertEqual(r_copy.width, r.width)
        self.assertEqual(r_copy.height, r.height)
        self.assertEqual(r_copy.x, r.x)
        self.assertEqual(r_copy.y, r.y)

    def test_create_square(self):
        """ tests create function
            test by creating squares
        """
        s = Square(1)
        s_dict = s.to_dictionary()
        s_copy = Square.create(**s_dict)
        self.assertIsInstance(s_copy, Square)
        self.assertEqual(s_copy.size, s.size)
        self.assertEqual(s_copy.x, s.x)
        self.assertEqual(s_copy.y, s.y)

    def test_create_invalid_class(self):
        """ tests create function when invalid class is passed """
        with self.assertRaises(TypeError):
            my_dict = {"id": 10}
            Base.create(**my_dict)
