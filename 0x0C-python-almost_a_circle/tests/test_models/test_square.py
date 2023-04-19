#!/usr/bin/python3
"""
Module has tests for the sqaure class

"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """ tests for the square class """

    def setUp(self):
        """ sets up resusable square instances """
        Base._Base__nb_objects = 0
        self.square = Square(10, 2, 1, 1000)
        self.square1 = Square(7)
        self.square2 = Square(5, 3, 4)
        self.square3 = Square(100, 4, 4)

    def tearDown(self):
        """ Deletes objects created """
        del self.square
        del self.square1
        del self.square2
        del self.square3

    def test_is_subclass(self):
        """ Test that squre inherits from rectangle """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_area(self):
        """ test area function """

        self.assertEqual(self.square.area(), self.square.height**2)
        self.assertEqual(self.square2.area(), self.square2.width**2)

    def test_id(self):
        """ test that id is set """
        self.square3.id = 5000

        self.assertEqual(self.square.id, 1000)
        self.assertEqual(self.square1.id, 1)
        self.assertEqual(self.square3.id, 5000)

    def test_height(self):
        """ test height is set correctly """
        self.assertEqual(self.square.height, 10)
        self.assertEqual(self.square1.height, 7)

        self.square3.height = 2000
        self.assertEqual(self.square3.height, 2000)

    def test_width(self):
        """ test width is set correctly """
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square1.width, 7)

        self.square3.width = 20
        self.assertEqual(self.square3.width, 20)

    def test_x(self):
        """ test x is set correctly """
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square1.x, 0)

        self.square2.x = 100
        self.assertEqual(self.square2.x, 100)

    def test_y(self):
        """ test y is set correctly """
        self.assertEqual(self.square.y, 1)
        self.assertEqual(self.square1.y, 0)

        self.square2.y = 15
        self.assertEqual(self.square2.y, 15)

    def test_str(self):
        """ tests __str__ """
        expected_output = "[Square] ({}) {}/{} - {}"\
            .format(self.square.id, self.square.x, self.square.y,
                    self.square.height)
        actual_output = str(self.square)
        self.assertEqual(expected_output, actual_output)

    def test_invalid_types_size_setter(self):
        """ tests the size setter when passed incorrect types"""
        invalid_types = [3.5, "str", [1, 2], ('0', 3)]

        for invalid in invalid_types:
            with self.assertRaises(TypeError) as e:
                self.square.size = invalid
            error_msg = str(e.exception)
            expected_msg = "width must be an integer"
            self.assertEqual(error_msg, expected_msg)

    def test_invalid_values_size_setter(self):
        """ tests the size setter when passed incorrect values """
        invalid_values = [-100, 0]

        for invalid in invalid_values:
            with self.assertRaises(ValueError) as e:
                self.square.size = invalid
            error_msg = str(e.exception)
            expected_msg = "width must be > 0"
            self.assertEqual(error_msg, expected_msg)

    def test_size_sets_width_height(self):
        """ test size getter works and setter sets width and height """
        current_value = self.square.size
        new_value = current_value + 5

        self.square.size = new_value

        self.assertTrue(current_value != self.square.size)
        self.assertEqual(self.square.width, new_value)
        self.assertEqual(self.square.height, new_value)

    def test_update(self):
        """ tests the update method """
        new_id = 4000
        new_size = 600
        new_x = 100
        new_y = 200
        self.square.update(new_id)
        self.square.update(new_id, new_size)
        self.square.update(new_id, new_size, new_x)
        self.square.update(new_id, new_size, new_x, new_y)
        self.square.update(new_id, new_size, new_x, new_y, 3, 4)

        expected_str = "[Square] ({}) {}/{} - {}"\
            .format(new_id, new_x, new_y, new_size)

        actual_str = str(self.square)
        self.assertEqual(actual_str, expected_str)

    def test_update_with_kwargs(self):
        """ test kwargs """
        old_id = self.square2.id
        self.square2.update(id=0)

        self.assertEqual(self.square2.id, 0)
        self.assertNotEqual(self.square2.id, old_id)

        self.square3.update(id=2, x=10, size=1000, y=5)
        expected_str = "[Square] (2) 10/5 - 1000"
        actual_str = str(self.square3)
        self.assertEqual(expected_str, actual_str)

        data = {'id': 100, 'size': 5, 'x': 0, 'y': 0}

        self.square1.update(**data)

        expected_str = "[Square] (100) 0/0 - 5"
        actual_str = str(self.square1)
        self.assertEqual(expected_str, actual_str)

        self.new_square = Square(56, 9, 10, 23)
        self.new_square.update(77, id=78)
        self.assertEqual(self.new_square.id, 77)
        self.assertNotEqual(self.new_square.id, 78)

    def test_to_dictionary(self):
        """ test to_dictionary function in square class """
        self.square_t = Square(50, 3, 3, 1)
        sq_dict = self.square_t.to_dictionary()

        my_dict = {'id': 1, 'size': 50, 'x': 3, 'y': 3}

        self.assertEqual(sq_dict, my_dict)
        self.assertIs(type(sq_dict), dict)
