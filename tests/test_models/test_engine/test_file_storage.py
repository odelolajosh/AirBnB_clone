#!/usr/bin/python3
"""
This module contains unittests for the `FileStorage` class
"""
import json
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage

classes = [Amenity, BaseModel, City, Place, Review, State, User]
test_json = "file.test.json"


class TestFileStorage(unittest.TestCase):
    """ Test suites for the `FileStorage` class """

    def setUp(self):
        """ Setup the `FileStorage` for testing """
        self.fs = FileStorage()
        self.prev__objects = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        self.prev__file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = test_json
        try:
            os.remove(test_json)
        except Exception:
            pass

    def tearDown(self):
        """ Restore `FileStorage` defaults """
        FileStorage._FileStorage__objects = self.prev__objects
        FileStorage._FileStorage__file_path = self.prev__file_path
        try:
            os.remove(test_json)
        except Exception:
            pass

    def test_new_instance(self):
        """ Test default instantiation if a `FileStorage` """
        all_objs = self.fs.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIs(all_objs, self.fs._FileStorage__objects)

    def test_new(self):
        """ Test the `new` method of FileStorage """
        c_objects = {}
        for cls in classes:
            with self.subTest(cls=cls):
                instance = cls()
                instance_key = cls.__name__ + "." + instance.id
                self.fs.new(instance)
                c_objects[instance_key] = instance
                self.assertEqual(c_objects, self.fs._FileStorage__objects)

    def test_save(self):
        """ Test objects are properly save in the `__file_path` """
        c_json = {}
        for cls in classes:
            instance = cls()
            instance_key = cls.__name__ + "." + instance.id
            self.fs.new(instance)
            c_json[instance_key] = instance.to_dict()
        self.fs.save()
        with open(test_json, "r") as fp:
            self.assertEqual(json.load(fp), c_json)

    def test_reload(self):
        """ Test that objects are reloaded properly """
        c_objects = {}
        fs__objects = {}
        for cls in classes:
            self.fs.new(cls())
        self.fs.save()
        FileStorage._FileStorage__objects = {}
        self.fs.reload()
        with open(test_json, "r") as fp:
            c_objects = json.load(fp)

        for k, v in self.fs.all().items():
            fs__objects[k] = v.to_dict()

        self.assertEqual(c_objects, fs__objects)


if __name__ == "__main__":
    unittest.main()
