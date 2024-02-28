#!/usr/bin/python3
"""base class for console"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """initialise the id and the created at and updated at dates"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """method that displays instance attributes in a user friendly way"""
        return str(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """method that updates update_at instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """show the instance attributes and class of an instance"""
        directory = self.__dict__
        directory["__class__"] = self.__class__.__name__
        directory["created_at"] = datetime.isoformat(directory["created_at"])
        directory["updated_at"] = datetime.isoformat(directory["updated_at"])
        return self.__dict__
