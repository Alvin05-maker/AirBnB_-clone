#!/usr/bin/python3
"""Defines a class user derieed from the class BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of User class.
    Attributes:
        email(str) : user's email.
        password(str): user's password.
        first_name(str): user's first name.
        last_name(str): user's last_name.
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
