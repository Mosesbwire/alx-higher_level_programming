#!/usr/bin/python3
"""
Test area()  function of the rectangle class

"""
import unittest
from models.rectangle import Rectangle


class TestArea(unittest.TestCase):
    """ Tests for area function """

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
