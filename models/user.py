#!/usr/bin/python3
"""
This module provides the `User` class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines a `User` class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
