#!/usr/bin/python3
"""
This module provides the `Review` class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines a `Review` class """
    place_id = ""
    user_id = ""
    text = ""
