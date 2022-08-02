#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
from datetime import datetime
from time import sleep
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test suites for the `BaseModel` class """

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        m1 = BaseModel()
        self.assertIsNotNone(m1)

    def test_attribute(self):
        """ Test presence of required attributes """
        m1 = BaseModel()
        m1_dict = m1.__dict__
        self.assertIn("id", m1_dict)
        self.assertIn("created_at", m1_dict)
        self.assertIn("updated_at", m1_dict)

    def test_unique_id(self):
        """ Test unique id """
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1, m2)

    def test_attribute_type(self):
        """ Test attribute type """
        m1 = BaseModel()
        self.assertIsInstance(m1.id, str)
        self.assertIsInstance(m1.created_at, datetime)
        self.assertIsInstance(m1.updated_at, datetime)
        self.assertIsInstance(m1.to_dict(), dict)

    def test_created_at(self):
        """ Test `created_at` and `updated_at` field """
        m = BaseModel()
        self.assertEqual(m.created_at, m.updated_at)
        ct_stamp = datetime.now().timestamp()
        # Test the time created equals the current time approx.
        self.assertAlmostEqual(m.created_at.timestamp(), ct_stamp, 0)

    def test_updated_at_save(self):
        """ Test `updated_at` value in  `save` method """
        m1 = BaseModel()
        diff = m1.updated_at - m1.created_at
        self.assertEqual(m1.created_at, m1.updated_at)
        self.assertAlmostEqual(diff.total_seconds(), 0, 2)
        sleep(0.1)  # sleep by 0.1s
        m1.save()
        diff = m1.updated_at - m1.created_at
        self.assertNotEqual(m1.created_at, m1.updated_at)
        # test the difference should be 0.1 approx.
        self.assertAlmostEqual(diff.total_seconds(), 0.1, 0)

    def test_to_dict(self):
        """ Test `to_dict` method """
        m1 = BaseModel()
        m_json = m1.to_dict()
        self.assertIsInstance(m_json, dict)
        # Checks if m1.__dict__ is a subset of m_json
        # should be false due to type differene in `updated_at`
        # and `created_at` fields
        self.assertFalse(dict(m_json, **m1.__dict__) == m_json)
        # values should be of type int, float or str
        self.assertTrue(all([
            type(v) in [int, float, str] for v in m_json.values()
        ]))
        self.assertIsInstance(m_json["created_at"], str)
        self.assertIsInstance(m_json["updated_at"], str)
        self.assertIn("__class__", m_json)
