#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test suites for the `BaseModel` class """

    def setUp(self):
        """ Setup the `Amenity` instance """
        self.a = Amenity()
        self.name = Amenity.__name__

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        self.assertIsNotNone(self.a)
        self.assertIsInstance(self.a, BaseModel)

    def test_attributes(self):
        """ Test presence of required attributes """
        self.assertTrue(hasattr(self.a, 'name'))

    def test_to_str(self):
        """ Test that the str method has the correct output """
        string = "[{}] ({}) {}".format(self.name, self.a.id, self.a.__dict__)
        self.assertEqual(string, str(self.a))


if __name__ == "__main__":
    unittest.main()
