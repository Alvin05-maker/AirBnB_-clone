#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instance_created
    TestBaseModel_save
    TestBaseModel_dict
"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel_instance_created(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_StoredInstance_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_is_id_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_is_updated_at__public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_uuids(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)
    def test_args_unused(self):
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemodel.__dict__.values()

class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "dict")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("dict", "file.json")
        except IOError:
            pass

    def test_save_argumented(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.save(None)

    def test_save_updates_file(self):
        basemodel = BaseModel()
        basemodel.save()
        basemodelid = "BaseModel." + basemodel.id
        with open("file.json", "r") as rf:
            self.assertIn(basemodelid, rf.read())


class TestBaseModel_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        basemodel = BaseModel()
        self.assertTrue(dict, type(basemodel.to_dict()))

    def test_to_dict_contains_actual_keys(self):
        basemodel = BaseModel()
        self.assertIn("id", basemodel.to_dict())
        self.assertIn("created_at", basemodel.to_dict())
        self.assertIn("updated_at", basemodel.to_dict())
        self.assertIn("__class__", basemodel.to_dict())

    def test_to_dict_has_extra_attributes(self):
        basemodel = BaseModel()
        basemodel.name = "Holberton"
        basemodel.my_number = 100
        self.assertIn("name", basemodel.to_dict())
        self.assertIn("my_number", basemodel.to_dict())

    def test_to_dict_datetime_attributes_are_strings(self):
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(str, type(basemodel_dict["created_at"]))
        self.assertEqual(str, type(basemodel_dict["updated_at"]))

    def test_to_dict_contrast(self):
        basemodel = BaseModel()
        self.assertNotEqual(basemodel.to_dict(), basemodel.__dict__)

    def test_to_dict_argumented(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.to_dict(None)


if __name__ == "__main__":
    unittest.main()
