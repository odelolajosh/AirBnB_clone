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
        self.name = City.__name__

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        self.assertIsNotNone(self.c)
        self.assertIsInstance(self.c, BaseModel)

    def test_attributes(self):
        """ Test presence of required attributes """
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))

    def test_defaults(self):
        """ Test default values """
        self.assertEqual(self.c.state_id, "")
        self.assertEqual(self.c.name, "")

    def test_to_str(self):
        """ Test that the str method has the correct output """
        string = "[{}] ({}) {}".format(self.name, self.c.id, self.c.__dict__)
        self.assertEqual(string, str(self.c))


if __name__ == "__main__":
    unittest.main()
