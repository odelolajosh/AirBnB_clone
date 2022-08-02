#!/usr/bin/python3
"""
The console module provides the `HBNBCommand` class for AirBnb
command intepreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class defines `AirBnb` line-oriented interpreter"""
    intro = ""
    prompt: str = "(hbnb) "

    def do_quit(self, arg):
        """ Quit the console session """
        return True

    def do_EOF(self, arg):
        """ Quits the console session """
        return True

    def emptyline(self):
        """ Respond to empty line command """
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
