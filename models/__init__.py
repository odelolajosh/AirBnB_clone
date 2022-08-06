#!/usr/bin/python3
"""
Make modules exportable
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
