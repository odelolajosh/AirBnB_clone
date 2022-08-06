#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test suites for the `BaseModel` class """

    def setUp(self):
        """ Setup the city instance """
        self.r = Review()
        self.name = Review.__name__

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        self.assertIsNotNone(self.r)
        self.assertIsInstance(self.r, BaseModel)

    def test_attributes(self):
        """ Test presence of required attributes """
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))

    def test_defaults(self):
        """ Test default values """
        self.assertEqual(self.r.place_id, "")
        self.assertEqual(self.r.user_id, "")
        self.assertEqual(self.r.text, "")

    def test_to_str(self):
        """ Test that the str method has the correct output """
        string = "[{}] ({}) {}".format(self.name, self.r.id, self.r.__dict__)
        self.assertEqual(string, str(self.r))


if __name__ == "__main__":
    unittest.main()
