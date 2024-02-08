#!/usr/bin/python3
"""
test_base_model module that supplies all unittest cases for the base module.
"""
import unittest
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Unit test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Sets up a BaseModel object for testing.
        """
        self.base_model = BaseModel()

    def test_public_instance_attributes(self):
        """
        Unit test if BaseModel object has all the required attributes.
        """

        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        """
        Unit test case if the id attribute is a valid UUID.
        """

        self.assertIsInstance(self.base_model.id, str)

        # A valid UUID has 36 characters, including hyphens.
        self.assertEqual(len(self.base_model.id), 36)

        # Check if Id is in UUID format.
        try:
            uuid.UUID(self.base_model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUId.")

    def test_str_method(self):
        """
        Test if the __str__ method returns the expected string representation.
        """
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)

        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method_updates_updated_at(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns the expected dictionary
        representation.
        """
        obj = self.base_model

        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

        # Test if to_dict method includes all instance attributes
        for attr, value in obj.__dict__.items():
            if attr not in ['created_at', 'updated_at']:
                self.assertIn(attr, obj_dict)
                self.assertEqual(obj_dict[attr], value)
