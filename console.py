#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
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