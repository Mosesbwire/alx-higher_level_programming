#!/usr/bin/python3
"""
Test module for the Rectangle class

"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Test class for the Rectangle
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_is_subclass_base(self):
        """ tests that rectangle inherits/ is subclass of Base """
        self.rectangle = Rectangle(20, 10, 15, 5)

        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIn('id', dir(self.rectangle))

    def test_has_attributes(self):
        """ tests that rectangle has attributes height, width, x, y """

        self.rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertIn('_Rectangle__width', dir(self.rectangle))
        self.assertIn('_Rectangle__height', dir(self.rectangle))
        self.assertIn('_Rectangle__x', dir(self.rectangle))
        self.assertIn('_Rectangle__y', dir(self.rectangle))

    def test_private_attributes(self):
        """ tests that height, width, x and y are private variables """

        self.rectangle = Rectangle(10, 5, 100, 200, 1000)
        with self.assertRaises(AttributeError,
                               msg="width is a private variable"):
            self.rectangle.__width
        with self.assertRaises(AttributeError,
                               msg="heigt is a private variable"):
            self.rectangle.__height
        with self.assertRaises(AttributeError, msg="x is a private variable"):
            self.rectangle.__x
        with self.assertRaises(AttributeError, msg="y is a private variable"):
            self.rectangle.__y

    def test_width_getters_setter(self):
        """ tests that __width has public getters and setters
            tests getter and setter work correctly
        """
        self.assertIn('width', dir(Rectangle))
        widths = [10, 20, 5, 1, 10000000000, 1500]

        for width in widths:
            self.rectangle = Rectangle(width, 20, 1, 1)
            self.assertEqual(self.rectangle.width, width)

    def test_type_width(self):
        """ tests that width raises typeError if value passed is not int """
        width = ["str", (1, 2), {'width': 10}, {100, 200}, [8, 9], 5.5, 0.45]
        for item in width:
            with self.assertRaises(TypeError)as e:
                self.rectangle_str = Rectangle(item, 2, 3, 4, 5)

        exception_msg = str(e.exception)
        actual_msg = "width must be an integer"
        self.assertEqual(exception_msg, actual_msg)

    def test_value_width(self):
        """ tests that valueError is raised if value is <= 0 """
        width = [0, -5, -1, -100]
        for item in width:
            with self.assertRaises(ValueError)as e:
                self.rectangle = Rectangle(item, 2, 3, 4, 5)
            exception_msg = str(e.exception)
            actual_msg = "width must be > 0"
            self.assertEqual(exception_msg, actual_msg)

    def test_height_getters_setter(self):
        """ tests that __height has public getters and setters"""
        self.assertIn('height', dir(Rectangle))
        heights = [1, 5, 7, 1000000000, 100000, 1500, 800]

        for height in heights:
            self.rectangle = Rectangle(1, height, 20, 10, 5)
            self.assertEqual(self.rectangle.height, height)

    def test_type_width(self):
        """ tests that height raises typeError if value passed is not int """
        height = ["str", (1, 2), {'width': 10}, {100, 200}, [8, 9], 5.5, 0.45]
        for item in height:
            with self.assertRaises(TypeError)as e:
                self.rectangle_str = Rectangle(20, item, 3, 4, 5)

        exception_msg = str(e.exception)
        actual_msg = "height must be an integer"
        self.assertEqual(exception_msg, actual_msg)

    def test_value_height(self):
        """ tests that valueError is raised if value is <= 0 """
        height = [0, -5, -1, -100]
        for item in height:
            with self.assertRaises(ValueError)as e:
                self.rectangle = Rectangle(10, item, 3, 4, 5)
            exception_msg = str(e.exception)
            actual_msg = "height must be > 0"
            self.assertEqual(exception_msg, actual_msg)

    def test_X_getters_setter(self):
        """ tests that __x has public getters and setters
            tests getter and setter work correctly
        """
        self.assertIn('x', dir(Rectangle))
        values = [10, 20, 5, 1, 10000000000, 1500]

        for value in values:
            self.rectangle = Rectangle(10, 20, value, 1)
            self.assertEqual(self.rectangle.x, value)

    def test_type_x(self):
        """ tests that x raises typeError if value passed is not int """
        values = ["str", (1, 2), {'width': 10}, {100, 200}, [8, 9], 5.5, 0.45]
        for value in values:
            with self.assertRaises(TypeError)as e:
                self.rectangle = Rectangle(10, 2, value, 4, 5)

        exception_msg = str(e.exception)
        actual_msg = "x must be an integer"
        self.assertEqual(exception_msg, actual_msg)

    def test_value_X(self):
        """ tests that valueError is raised if value is < 0 """
        values = [-2000, -5, -1, -100]
        for value in values:
            with self.assertRaises(ValueError)as e:
                self.rectangle = Rectangle(10, 2, value, 4, 5)
            exception_msg = str(e.exception)
            actual_msg = "x must be >= 0"
            self.assertEqual(exception_msg, actual_msg)

    def test_Y_getters_setter(self):
        """ tests that __y has public getters and setters
            tests getter and setter work correctly
        """
        self.assertIn('y', dir(Rectangle))
        values = [10, 20, 5, 1, 10000000000, 1500]

        for value in values:
            self.rectangle = Rectangle(10, 20, 1, value)
            self.assertEqual(self.rectangle.y, value)

    def test_type_y(self):
        """ tests that y raises typeError if value passed is not int """
        values = ["str", (1, 2), {'width': 10}, {100, 200}, [8, 9], 5.5, 0.45]
        for value in values:
            with self.assertRaises(TypeError)as e:
                self.rectangle = Rectangle(1, 2, 3, value, 5)

        exception_msg = str(e.exception)
        actual_msg = "y must be an integer"
        self.assertEqual(exception_msg, actual_msg)

    def test_value_y(self):
        """ tests that valueError is raised if value is < 0 """
        values = [-100, -5, -1, -100]
        for value in values:
            with self.assertRaises(ValueError)as e:
                self.rectangle = Rectangle(1, 2, 3, value, 5)
            exception_msg = str(e.exception)
            actual_msg = "y must be >= 0"
            self.assertEqual(exception_msg, actual_msg)

    def test_required_args(self):
        """ Tests that required args are passed in"""

        with self.assertRaises(TypeError)as e:
            self.rectangle = Rectangle()
        exception_msg = str(e.exception)
        actual_msg = ".__init__() missing 2 required\
                positional arguments: \'width\' and \'height\'"

    def test_default_args(self):
        """ Tests that optional args have their default values """
        self.rectangle = Rectangle(10, 10)
        self.assertEqual(self.rectangle.y, 0)
        self.assertEqual(self.rectangle.x, 0)
        self.assertEqual(self.rectangle.id, 1)

    def test_area(self):
        """ tests for correct output of area """
        widths = [10, 5, 6, 1, 2000, 1000000, 15]
        heights = [18, 5, 16, 5, 11, 44443249, 7]

        for width in widths:
            for height in heights:
                self.rect = Rectangle(width, height)
                self.assertEqual(self.rect.area(), width * height)

    def test_attribute_area(self):
        """ tests that the function is available """
        self.assertIn('area', dir(Rectangle))

    def test_print_output(self):
        """
        Test method to assert that a specific value has been printed to stdout.
        """
        self.rect = Rectangle(2, 3, 2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.rect.display()
        expected_output = "\n\n  ##\n  ##\n  ##"
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_attribute_display(self):
        """ Test method to assert that function display is available """
        self.assertIn('display', dir(Rectangle))

    def test_str(self):
        """ tests that __str__ has been overridden """
        self.rect1 = Rectangle(10, 10)
        self.rect2 = Rectangle(4, 4, 1, 3)
        self.rect3 = Rectangle(5, 100, 5, 6, 1000)

        obj_list = [self.rect1, self.rect2, self.rect3]

        for obj in obj_list:
            msg = "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(obj.id, obj.x, obj.y, obj.width, obj.height)
            self.assertEqual(msg, str(obj))

    def test_update(self):
        """ tests the update function
        updates the attributes of the rectangle

        """
        test_id = 1000
        width = 20
        height = 30
        x = 4
        y = 5
        self.rect = Rectangle(width, height, x, y, test_id)
        self.rect.update(100)
        self.assertEqual(self.rect.id, 100)
        self.assertNotEqual(test_id, self.rect.id)

        self.rect.update(100, 200)
        self.assertEqual(self.rect.width, 200)
        self.assertNotEqual(width, self.rect.width)

        self.rect.update(100, 200, 300)
        self.assertEqual(self.rect.height, 300)
        self.assertNotEqual(height, self.rect.width)

        self.rect.update(100, 200, 300, 40)
        self.assertEqual(self.rect.x, 40)
        self.assertNotEqual(x, self.rect.x)

        self.rect.update(100, 200, 300, 40, 50)
        self.assertEqual(self.rect.y, 50)
        self.assertNotEqual(y, self.rect.y)

        self.rect.update()
        self.assertEqual(self.rect.id, 100)
        self.assertEqual(self.rect.width, 200)
        self.assertEqual(self.rect.height, 300)
        self.assertEqual(self.rect.x, 40)
        self.assertEqual(self.rect.y, 50)

        self.rect2 = Rectangle(width, height, x, y, test_id)

        self.rect2.update(height=1)
        self.assertEqual(self.rect2.height, 1)

        self.rect2.update(id=2, x=77)
        self.assertEqual(self.rect2.id, 2)
        self.assertEqual(self.rect2.x, 77)

        self.rect2.update(5000, id=100)
        self.assertEqual(self.rect2.id, 5000)
        self.assertNotEqual(self.rect2.id, 100)

        with self.assertRaises(AttributeError) as e:
            self.rect2.update(val=2)
        actual_msg = "val is not an instance variable"
        expected_msg = str(e.exception)
        self.assertEqual(actual_msg, expected_msg)

    def test_to_dictionary(self):
        """ test to_dictionary function in rectangle class """
        self.rect = Rectangle(20, 10, 5, 5, 1000)

        rect_dict = self.rect.to_dictionary()
        my_dict = {'id': 1000, 'width': 20, 'height': 10, 'x': 5, 'y': 5}

        self.assertEqual(rect_dict, my_dict)
        self.assertIs(type(rect_dict), dict)
