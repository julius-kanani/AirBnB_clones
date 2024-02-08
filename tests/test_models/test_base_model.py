#!/usr/bin/python3
"""
test_base_model module that supplies all unittest cases for the base module.
"""
import unittest
from models.base_model import BaseModel


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
