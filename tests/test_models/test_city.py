#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Test suites for the `BaseModel` class """

    def setUp(self):
        """ Setup the city instance """
        self.c = City()

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        self.assertIsNotNone(self.c)
        self.assertIsInstance(self.c, BaseModel)

    def test_attributes(self):
        """ Test presence of required attributes """
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))


if __name__ == "__main__":
    unittest.main()
