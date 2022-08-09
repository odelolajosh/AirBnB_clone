#!/usr/bin/python3
"""
The console module provides the `HBNBCommand` class for AirBnb
command intepreter.
"""

import cmd
import re
import shlex
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class defines `AirBnb` line-oriented interpreter"""
    intro = ""
    prompt: str = "(hbnb) "

    c_names = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """ Quit the console session """
        return True

    def do_EOF(self, arg):
        """ Quits the console session """
        print()
        return True

    def help_show(self):
        """ Help for the `show` command """
        h_msg = [
            "Prints the string rep of a class instance based on the id.",
            "Usage: show <class name> <id>"
        ]
        print("\n".join(h_msg))

    def help_all(self):
        """ Help for the `all` command """
        h_msg = [
            "Prints all string rep of all instances optionally with class.",
            "Usage: all <class name?>"
        ]
        print("\n".join(h_msg))

    def help_create(self):
        """ Help for the `create` command """
        h_msg = [
            "Creates a new instance of a class.",
            "Usage: create <class name>"
        ]
        print("\n".join(h_msg))

    def help_destroy(self):
        """ Help for the `destroy` command """
        h_msg = [
            "Deletes a new instance of a class using id.",
            "Usage: destroy <class name> <id>"
        ]
        print("\n".join(h_msg))

    def help_update(self):
        """ Help for the `update` command """
        h_msg = [
            "Updates an instance of a class using id and key-value pair.",
            "Usage: update <class name> <id> <key> <value>"
        ]
        print("\n".join(h_msg))

    def help_count(self):
        """ Help for the `count` command """
        h_msg = [
            "Display the count instances in a class.",
            "Usage: count <class name>"
        ]
        print("\n".join(h_msg))

    def emptyline(self):
        """ Respond to empty line command """
        pass

    def precmd(self, line: str) -> str:
        """
        Hook method executed just before the command
        line is interpreted, but after the input prompt is
        generated and issued.
        """
        matches = re.findall(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if matches:  # array is not empty
            [cls, method, params] = matches[0]
            args = params = str(params).strip()
            if params:
                args = params.replace(", ", " ")
            return "{} {} {}".format(method, cls, args)

        return super().precmd(line)

    def do_create(self, arg):
        """ Creates a new instance of `BaseModel` """
        if len(arg) == 0:
            print("** class name missing **")
            return False

        if arg not in HBNBCommand.c_names.keys():
            print("** class doesn't exist **")
            return False

        m = HBNBCommand.c_names[arg]()
        m.save()
        print(m.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the className
        """
        arr = self.__get_class_args(arg)
        if not arr:
            return False

        if len(arr) < 2:
            print("** instance id missing **")
            return False

        cls, id = arr[0], arr[1]
        key = "{}.{}".format(cls, id)

        if key not in storage.all():
            print("** no instance found **")
        else:
            obj = storage.all()[key]
            print(obj)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        arr = self.__get_class_args(arg)
        if not arr:
            return False

        if len(arr) < 2:
            print("** instance id missing **")
            return False

        cls, id = arr[0], arr[1]
        key = "{}.{}".format(cls, id)

        if key not in storage.all():
            print("** no instance found **")
        else:
            # using name mangling `storage._FileStorage__objects`
            # del storage._FileStorage__objects[key]
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        cls = None
        if arg:
            arr = self.__get_class_args(arg)
            if not arr:     # class name is not valid?
                return False
            cls = arr[0]

        if not cls:     # get all
            print([str(v) for v in storage.all().values()])
        else:
            print([
                str(v)
                for k, v in storage.all().items()
                if str(k).split(".")[0] == cls
            ])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        arr = self.__get_class_args(arg)
        if not arr:
            return False

        if len(arr) < 2:
            print("** instance id missing **")
            return False

        cls, id = arr[0], arr[1]
        key = "{}.{}".format(cls, id)

        if key not in storage.all():
            print("** no instance found **")
            return False

        obj = storage.all()[key]
        if len(arr) < 3:
            print("** attribute name missing **")
            return False

        dict = self.__parse_dict(arr[2])

        if not dict and len(arr) < 4:
            print("** value missing **")
            return False

        if not dict:
            attr, val = arr[2], arr[3]
            dict = [[attr, val]]

        for [attr, val] in dict:
            setattr(obj, attr, val)
        obj.save()

    def do_count(self, arg):
        """ Get count of persisted instances """
        cls = None
        if arg:
            arr = self.__get_class_args(arg)
            if not arr:     # class name is not valid?
                return False
            cls = arr[0]

        if not cls:     # get all
            print(len([str(v) for v in storage.all().values()]))
        else:
            print(len([
                str(v)
                for k, v in storage.all().items()
                if str(k).split(".")[0] == cls
            ]))

    def __get_class_args(self, arg: str):
        """
        Gets the arguments in a command
        Format: <class_name> (...params)
        """
        if not arg:
            print("** class name missing **")
            return None

        d_split = re.findall(r"^(.+)\s(\{.+\})", arg)
        if d_split:
            rest, dict = d_split[0]
            s_args = shlex.split(rest) + [dict]
        else:
            s_args = shlex.split(arg)

        if s_args[0] not in HBNBCommand.c_names.keys():
            print("** class doesn't exist **")
            return None

        return s_args

    def __parse_dict(self, arg: str):
        """
        Parse a dictionary like argument
        """
        if not arg:
            return None

        if re.match(r"\{.*\}", arg) is None:            # not in dict format
            return None

        unbraced = arg.rstrip("}").lstrip("{").strip()
        normalized = unbraced.replace(", ", ",").replace(": ", ":")
        argv = [k_v.split(":") for k_v in normalized.split(",")]
        if not all([len(kv) == 2 for kv in argv]):
            return None

        # normalized argv
        for i, pair in enumerate(argv):
            [key, value] = pair
            argv[i][0] = key.strip("'").strip('"')
            if not re.match(r"[\'|\"].*[\'|\"]", value):    # is not quoted
                if re.match(r"^\d+$", value):    # is an int
                    argv[i][1] = int(value)
                elif re.match(r"^\d+\.\d+?$", value):    # is a float
                    argv[i][1] = float(value)
            else:    # quoted, taken as str
                argv[i][1] = value.strip("'").strip('"')

        return argv


if __name__ == "__main__":
    HBNBCommand().cmdloop()
