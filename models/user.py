#!/usr/bin/python3
"""user class file"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class file"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
