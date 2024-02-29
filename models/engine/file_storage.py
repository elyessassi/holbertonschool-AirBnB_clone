#!/usr/bin/python3
"""file storage class"""

import json
import os


class FileStorage():
    __file_path = ""
    __objects = {}

    def all(self):
        """return the dictionary _objects"""
        return self.__object

    def new(self, obj):
        """add a new object to the dictionary"""
        self.__objects[f"{self.__class__.__name__}.{self.id}"] = obj

    def save(self):
        """save __objects to JSON file"""
        with open(self.__filepath, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserialize JSON file to __objects"""
        if os.path.isfile(self.__file_path) is True:
            with open(self.__filepath, "r") as f:
                self.__objects = json.load(f)
