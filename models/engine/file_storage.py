#!/usr/bin/python3
"""file storage class"""

import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary _objects"""
        return self.__objects

    def new(self, obj):
        """add a new object to the dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save __objects to JSON file"""
        objs = self.__objects
        tempdict = {}
        for key, value in objs.items():
            tempdict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(tempdict, f)

    def reload(self):
        """deserialize JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        
        if os.path.isfile(self.__file_path) is True:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    theclassname, theid = key.split(".")
                    classname = eval(theclassname)
                    self.__objects[key] = classname(**value)
            

