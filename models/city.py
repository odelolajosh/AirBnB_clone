#!/usr/bin/python3
"""
This module provides the `City` class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines a `City` class """
    state_id = ""
    name = ""
