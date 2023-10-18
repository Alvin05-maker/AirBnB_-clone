#!/usr/bin/python3
""" Defines all common attributes/methods for other classes."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Base class for other classes to inherit from."""
    def __init__(self, *args, **kwargs):
        """ Initialize the base model.

        Args:
            *args(any)): Arbitrary positional arguments
            **kwargs(dict): Key/value pair arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        strtimeformat = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if isinstance(value, datetime):
                        value = value.isoformat()
                    self.__dict__[key] = datetime.strptime(value, strtimeformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updates the attribute updated_at with the current time"""
        self.updated_at = datetime.today()
        models.storage.save()
    def to_dict(self):
        """Returns the dictionary representation of object instances"""
        dict_rep = self.__dict__.copy()
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        dict_rep["__class__"] = self.__class__.__name__
        return dict_rep

    def __str__(self):
        """Return the string representation of the BaseModel instance"""
        return "[{}] ({}) {})".format(self.__class__.__name__, self.id, self.__dict__)
