#!/usr/bin/python3
"""
This module provides the `BaseModel` class.
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Define the `BaseModel` Class
    The `BaseModel` class defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """"Initialize attribute for `BaseModel` class"""
        if kwargs:  # kwargs?
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the string representation of the class"""
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """Persists instance"""
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        ins = self.__dict__.copy()
        ins["__class__"] = self.__class__.__name__
        ins["created_at"] = datetime.isoformat(ins["created_at"])
        ins["updated_at"] = datetime.isoformat(ins["updated_at"])
        return ins
