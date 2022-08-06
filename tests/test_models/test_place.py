#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test suites for the `BaseModel` class """

    def setUp(self):
        """ Setup the `Place` instance """
        self.pl = Place()
        self.name = Place.__name__

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        self.assertIsNotNone(self.pl)
        self.assertIsInstance(self.pl, BaseModel)

    def test_attributes(self):
        """ Test presence of required attributes """
        self.assertTrue(hasattr(self.pl, 'city_id'))
        self.assertTrue(hasattr(self.pl, 'user_id'))
        self.assertTrue(hasattr(self.pl, 'name'))
        self.assertTrue(hasattr(self.pl, 'description'))
        self.assertTrue(hasattr(self.pl, 'number_rooms'))
        self.assertTrue(hasattr(self.pl, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pl, 'max_guest'))
        self.assertTrue(hasattr(self.pl, 'price_by_night'))
        self.assertTrue(hasattr(self.pl, 'latitude'))
        self.assertTrue(hasattr(self.pl, 'longitude'))
        self.assertTrue(hasattr(self.pl, 'amenity_ids'))

    def test_to_str(self):
        """ Test that the str method has the correct output """
        string = "[{}] ({}) {}".format(self.name, self.pl.id, self.pl.__dict__)
        self.assertEqual(string, str(self.pl))


if __name__ == "__main__":
    unittest.main()
