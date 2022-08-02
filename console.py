#!/usr/bin/python3
"""
The console module provides the `HBNBCommand` class for AirBnb
command intepreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class defines `AirBnb` line-oriented interpreter"""
    pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
