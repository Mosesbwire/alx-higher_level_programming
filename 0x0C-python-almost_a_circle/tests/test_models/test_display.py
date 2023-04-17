#!/usr/bin/python3
"""
Module tests the display function of Rectangle class

"""
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestDisplay(unittest.TestCase):
    """ Contains test for the display function

    Test case to assert that a specific value has been printed to stdout.

    Example usage:
    >>> python -m unittest test_print_output.py

    This test case captures the output of a function\
            that is expected to print a specific value to stdout.
    It redirects stdout to a StringIO object, calls the function,\
            and then resets stdout to its original value.
    Finally, it asserts that the captured output matches\
            the expected value using the assertEqual method.
    """

    def test_print_output(self):
        """
        Test method to assert that a specific value has been printed to stdout.
        """
        self.rect = Rectangle(3, 3)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.rect.display()
        expected_output = "###\n###\n###"
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_attribute_display(self):
        """ Test method to assert that function display is available """
        self.assertIn('display', dir(Rectangle))
