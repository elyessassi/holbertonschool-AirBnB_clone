#!/usr/bin/python3
"""Cmd class file"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Cmd class"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, args):
        """press EOF key to exit program"""
        print("")
        return True
    
    def emptyline(self):
        """ignore the default behaviour of printing last command"""
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()