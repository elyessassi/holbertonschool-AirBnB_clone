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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """save __objects to JSON file"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserialize JSON file to __objects"""
        if os.path.isfile(self.__file_path) is True:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
