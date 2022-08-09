#!/usr/bin/python3
"""
This module contains unittests for the `BaseModel` class
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

test_json = "file.test.json"


class TestConsole(unittest.TestCase):
    """ Test suites for the `BaseModel` class """

    @classmethod
    def setUpClass(cls):
        """ Set up class for testing """
        cls.prev__file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = test_json
        cls.prev__objects = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        try:
            os.remove(test_json)
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """ Set up class for testing """
        FileStorage._FileStorage__file_path = cls.prev__file_path
        FileStorage._FileStorage__objects = cls.prev__objects
        try:
            os.remove(test_json)
        except Exception:
            pass
    
    def test_quit(self):
        """ Test the `quit` command """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("quit")
            f.seek(0)
            line = f.readline()
            self.assertEqual(line, '')
    
    def test_EOF(self):
        """ Test the `Ctrl + D` command """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("EOF")
            f.seek(0)
            line = f.readline()
            self.assertEqual(line, '\n')
    
    def test_empty(self):
        """ Test the `empty line` command """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("")
            f.seek(0)
            line = f.readline()
            self.assertEqual(line, '')
    
    def test_help(self):
        """ Test the `help` command """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("help")
            f.seek(0)
            line = f.read()
            expectedIn = "Documented commands (type help <topic>):"
            self.assertIn(expectedIn, line)
        

    def test_create(self):
        """ Test the `create` command """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("create User")
            f.seek(0)
            r_id = f.readline().rstrip("\n")
            key = "{}.{}".format(User.__name__, r_id)
            self.assertIn(key, storage.all())
            self.assertIsInstance(storage.all()[key], User)

    def test_create_with_no_class(self):
        """ Test the `create` command with no specified class """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("create")
            f.seek(0)
            expected = "** class name missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

    def test_create_with_wrong_class(self):
        """ Test the `create` command with no wrong class """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("create MyModel")
            f.seek(0)
            expected = "** class doesn't exist **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

    def test_show(self):
        """ Test the `show` command """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            r = Review()
            r.save()
            console.onecmd("show Review " + r.id)
            f.seek(0)
            actual = f.readline().rstrip("\n")
            self.assertEqual(str(r), actual)

    def test_show_with_invalid_command(self):
        """ Test the `show` command with no or invalid arguments """
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("show")
            f.seek(0)
            expected = "** class name missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("show MyModel")
            f.seek(0)
            expected = "** class doesn't exist **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("show State")
            f.seek(0)
            expected = "** instance id missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

    def test_show_with_bad_id(self):
        """ Test the `show` command with no wrong class """
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("show User " + s.id)
            f.seek(0)
            expected = "** no instance found **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("show State 1212")
            f.seek(0)
            expected = "** no instance found **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

    def test_destroy(self):
        """ Test the `destroy` command """
        a = Amenity()
        a.save()
        key = "{}.{}".format(Amenity.__name__, a.id)
        self.assertIn(key, storage.all())
        console = HBNBCommand()
        console.onecmd("destroy Amenity " + a.id)
        self.assertNotIn(key, storage.all())

    def test_destroy_with_invalid_command(self):
        """ Test the `destroy` command with no or invalid arguments """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("destroy")
            f.seek(0)
            expected = "** class name missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("destroy MyModel")
            f.seek(0)
            expected = "** class doesn't exist **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("destroy State")
            f.seek(0)
            expected = "** instance id missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

    def test_destroy_with_bad_id(self):
        """ Test the `destroy` command with no wrong class """
        c = City()
        c.save()
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("destroy Amenity " + c.id)
            f.seek(0)
            expected = "** no instance found **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("destroy State 1212")
            f.seek(0)
            expected = "** no instance found **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

    def test_all(self):
        """ Test the `all` command """
        FileStorage._FileStorage__objects = {}
        c_models = [State, Place, User, Amenity, Place, BaseModel]
        c_all = []
        for cls in c_models:
            model = cls()
            model.save()
            c_all.append(str(model))
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("all")
            f.seek(0)
            actual = f.read()
            expected = str(c_all) + '\n'
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("all Place")
            f.seek(0)
            actual = f.read()
            c_all_pl = [
                str for model, str in zip(c_models, c_all)
                if model is Place
            ]
            expected = str(c_all_pl) + '\n'
            self.assertEqual(actual, expected)
    
    def test_all_with_invalid_args(self):
        """ Test the `all` command with no or invalid arguments """
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("all MyModel")
            f.seek(0)
            expected = "** class doesn't exist **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

    def test_update(self):
        """ Test the `update` command """
        u = User()
        u.save()
        new_mail = "josh@me.self"
        console = HBNBCommand()
        self.assertEqual(u.email, "")
        console.onecmd("update User {} email {}".format(u.id, new_mail))
        key = "{}.{}".format(User.__name__, u.id)
        new_u = storage.all()[key]
        self.assertEqual(new_u.email, new_mail)

        # New attribute
        u = new_u
        new_age = '4'
        self.assertFalse(hasattr(u, 'age'))
        console.onecmd("update User {} age {}".format(u.id, new_age))
        new_u = storage.all()[key]
        self.assertEqual(new_u.age, new_age)

    def test_update_with_invalid_command(self):
        """ Test the `update` command with no or invalid arguments """
        s = State()
        s.save()
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("update")
            f.seek(0)
            expected = "** class name missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("update MyModel")
            f.seek(0)
            expected = "** class doesn't exist **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("update State")
            f.seek(0)
            expected = "** instance id missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("update State 123232")
            f.seek(0)
            expected = "** no instance found **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("update State {}".format(s.id))
            f.seek(0)
            expected = "** attribute name missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("update State {} name".format(s.id))
            f.seek(0)
            expected = "** value missing **"
            actual = f.readline().rstrip("\n")
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
