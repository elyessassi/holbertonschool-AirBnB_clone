#!/usr/bin/python3
"""base class for console"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initialise the id and the created_at and updated_at dates"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if (kwargs is not None):
            format = "%Y-%m-%dT%H:%M:%S.%f"
            try:
                self.id = kwargs["id"]
                x = datetime.strptime(kwargs["created_at"], format)
                y = datetime.strptime(kwargs["updated_at"], format)
                self.created_at = x
                self.updated_at = y
            except KeyError:
                pass
        storage.new(self)

    def __str__(self):
        """method that displays instance attributes in a user friendly way"""
        return str(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """method that updates update_at instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """show the instance attributes and class of an instance"""
        directory = self.__dict__.copy()
        directory["__class__"] = self.__class__.__name__
        directory["created_at"] = datetime.isoformat(directory["created_at"])
        directory["updated_at"] = datetime.isoformat(directory["updated_at"])
        return directory
