#!usr/bin/python3
"""
This module provides the `FileStorage` class.
The `FileStorage` class contain the implementation logic of the
serialization and deserialization of the `BaseModel` derivatives
all aims to provide persistence of the instances.
"""

import json
import os


class FileStorage:
    """ Defines the `FileStorage` class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Provides all the persisted `BaseModel` entities """
        return FileStorage.__objects

    def new(self, obj):
        """ Add a new obj to the `__objects` dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes `__objects` to the JSON file specified
        in `__file_path` """
        ins_s = {}

        for key, value in FileStorage.__objects.items():
            ins_s[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as fp:
            json.dump(ins_s, fp)

    def reload(self):
        """ Deserializes the JSON file to `__objects` """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as fp:
                from models.amenity import Amenity
                from models.base_model import BaseModel
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User

                c_names = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
                }
                for k,v in json.load(fp).items():
                    cls_s = k.split(".")[0]
                    self.new(c_names[cls_s](**v))
