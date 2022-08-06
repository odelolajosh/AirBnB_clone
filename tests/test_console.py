#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
from io import StringIO
import unittest
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ Test suites for the `BaseModel` class """
    def test_console(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")


if __name__ == "__main__":
    unittest.main()
