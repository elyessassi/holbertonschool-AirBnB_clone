#!/usr/bin/python3
"""Cmd class file"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


classnames = ["BaseModel", "User"]

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
    
    def do_create(self, args):
        """creates an instance and save it to JSON file"""
        if args == "":
            print("** class name missing **")
        elif args not in classnames:
            print("** class doesn't exist **")
        else:
            x = eval(args)
            print(type(x))
            x.save()
            print(x.id)
    
    def do_show(self, args):
        """print the string representation of an object based on the class name and id"""
        mylist = args.split()
        if args == "":
            print("** class name missing **")
        elif mylist[0] not in classnames:
            print("** class doesn't exist **")
        elif len(mylist) == 1:
            print("** instance id missing **")
        else:
            x = False
            dictionary = storage.all().copy()
            for key in dictionary.keys():
                if key == f"{mylist[0]}.{mylist[1]}":
                    print(dictionary[key])
                    x = True
                    break
            if (x == False):
                print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        mylist = args.split()
        if args == "":
            print("** class name missing **")
        elif mylist[0] not in classnames:
            print("** class doesn't exist **")
        elif len(mylist) == 1:
            print("** instance id missing **")
        else:
            x = False
            dictionary = storage.all()
            for key in dictionary.keys():
                if key == f"{mylist[0]}.{mylist[1]}":
                    del dictionary[key]
                    storage.save()
                    x = True
                    break
            if (x == False):
                print("** no instance found **")
        
    def do_all(self, args):
        """Print all string representation of all instances based or not on the class name"""
        dictionary = storage.all().copy()
        if args == "":
            for key in dictionary.keys():
                print(dictionary[key])
        elif args not in classnames:
            print("** class doesn't exist **")
        else:
            for key in dictionary.keys():
                classname, classid = key.split(".")
                if classname == args:
                    print(dictionary[key])
    
    def do_update(self, args):
        """Update an instance based on the class name and id by adding or updating attribute"""
        mylist = args.split()
        dictionary = storage.all()
        if args == "":
            print("** class name missing **")
        elif mylist[0] not in classnames:
            print("** class doesn't exist **")
        elif len(mylist) == 1:
            print("** instance id missing **")
        elif len(mylist) == 2:
            x = False
            for key in dictionary.keys():
                if key == f"{mylist[0]}.{mylist[1]}":
                    x = True
                    break
            if x == False:
                print("** no instance found **")
        elif len(mylist) == 3:
            print("** value missing **")
        else:
            for key in dictionary.keys():
                if key == f"{mylist[0]}.{mylist[1]}":
                    dictionary[key].mylist[2] == list[3]
            storage.save()





    


        

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()