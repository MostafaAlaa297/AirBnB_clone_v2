#!/usr/bin/env python3
"""
================
Test base module
================
"""

import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestBase(unittest.TestCase):
    """
    Test the base class
    """

    def setUp(self):
        """
        Executes once before each test case
        """
        self.my_model = BaseModel()

    def tearDown(self):
        """
        Cleans up after  each test case
        """
        storage_file = FileStorage._FileStorage__file_path
        if os.path.exists(storage_file):
            os.remove(storage_file)

    def test_attributes_on_creation(self):
        """
        Test attributes on creation
        """
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_id_uniqueness(self):
        """
        Test id uniqueness
        """
        obj = BaseModel()
        self.assertNotEqual(self.my_model.id, obj.id)

    def test_str_representaion(self):
        """
        Test __str__ representation
        """
        expected_str = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save_method(self):
        """
        Test save method updates updated_at
        """
        old_updated_at = self.my_model.save()
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method
        """
        self.my_model.name = "Test model"
        self.my_model.my_number = 55
        obj_dict = self.my_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], self.my_model.id)
        self.assertEqual(obj_dict["created_at"], self.my_model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], self.my_model.updated_at.isoformat())
        self.assertEqual(obj_dict["name"], "Test model")
        self.assertEqual(obj_dict["my_number"], 55)

    def test_id_is_not_none(self):
        """
        Tests if id is not none
        """
        self.assertIsNotNone(self.my_model.id, "Test value is none")

    def test_id_is_string(self):
        """
        Tests if id is a string
        """
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at_type_conversion(self):
        """
        Test created_at type conversion to string
        """
        created_at_str = self.my_model.to_dict()["created_at"]
        self.assertIsInstance(created_at_str, str)

    def test_updated_at_type_conversion(self):
        """
        Test updated_at type conversion to string
        """
        self.my_model.save()
        updated_at_str = self.my_model.to_dict()["updated_at"]
        self.assertIsInstance(updated_at_str, str)

    def test_reload(self):
        """
        Test reloading from the dictionary representaion
        """
        self.my_model.name = "Test reloading"
        self.my_model.save()
        storage = FileStorage()
        storage.reload()
        reloaded_objects = storage.all()
        self.assertIn("BaseModel." + self.my_model.id, reloaded_objects)

        obj_dict = self.my_model.to_dict()

        class_name = obj_dict["__class__"]
        del obj_dict["__class__"]
        reloaded_obj = globals()[class_name](**obj_dict)

        self.assertEqual(reloaded_obj.id, self.my_model.id)
        self.assertEqual(reloaded_obj.name, self.my_model.name)
        self.assertEqual(reloaded_obj.created_at, self.my_model.created_at)
        self.assertEqual(reloaded_obj.updated_at, self.my_model.updated_at)


if __name__ == "__main__":
    unittest.main()
