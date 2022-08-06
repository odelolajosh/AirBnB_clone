#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test suites for the `BaseModel` class """

    def setUp(self):
        """ Setup the state instance """
        self.s = State()

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        self.assertIsNotNone(self.s)
        self.assertIsInstance(self.s, BaseModel)

    def test_attributes(self):
        """ Test presence of required attributes """
        self.assertTrue(hasattr(self.s, 'name'))


if __name__ == "__main__":
    unittest.main()
