#!/usr/bin/python3
"""Cmd class file"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


classnames = ["BaseModel", "User", "Review", "City", "Place","State", "Amenity"]

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
            x = eval(args)()
            storage.save()
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
            dictionary = storage.all()
            if f"{mylist[0]}.{mylist[1]}" in dictionary:
                print(dictionary[f"{mylist[0]}.{mylist[1]}"])
            else:
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
        dictionary = storage.all()
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
            print("** attribute name missing **")
        elif len(mylist) == 3:
            print("** value missing **")
        else:
            x = False
            for key in dictionary.keys():
                if key == f"{mylist[0]}.{mylist[1]}":
                    if (mylist[3].isdigit()) == True:
                        dictionary[key].__dict__.update({mylist[2]:eval(mylist[3])})
                    elif (mylist[3].isdigit()) != True:
                        dictionary[key].__dict__.update({mylist[2]:str(mylist[3])})
                    x = True
            storage.save()
            if x == False:
                print("** instance id missing **")





    


        

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()