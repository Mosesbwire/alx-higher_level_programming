#!/usr/bin/python3
"""
this is the test module for the Base class

"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Contains tests for the base class """

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_nb_objects_is_private(self):
        """  tests the __nb_obect private variable"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_id_is_set(self):
        """ tests that id is set """
        self.base = Base()
        self.assertEqual(self.base.id, 1)
        self.base2 = Base()
        self.assertEqual(self.base2.id, 2)
        self.assertIsNotNone(self.base.id)
        self.assertIsNotNone(self.base2.id)

    def test_user_id_is_set(self):
        """ test id passed in by user is set """
        self.base = Base(100)
        self.assertEqual(self.base.id, 100)

    def test_id_not_incremented(self):
        """ test that id is not incremented when user passes in own id """
        self.assertEqual(Base._Base__nb_objects, 1)

        for i in range(4):
            self.base = Base(i)
        self.assertEqual(Base._Base__nb_objects, 1)
