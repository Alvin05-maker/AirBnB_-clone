#!/usr/bin/python3
""" Defines a class File storage that stores instance created"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        cls_objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cls_objname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = FileStorage.__objects
        object_dict = {obj: objdict[obj].to_dict() for obj in objdict.keys()}
        with open(FileStorage.__file_path, "w") as wf:
            json.dump(object_dict, wf)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                object_dict = json.load(f)
                for o in object_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
