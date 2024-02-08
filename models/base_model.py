#!/usr/bin/python3
"""
BaseModel module that supplies the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class with common attributes and methods for other classes.
    """

    def __init__(self):
        """
        Initialize a new instance of BaseModel with unique id and
        creation/update timestamps.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Update the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the instance attributes to a dictionary with additional
        metadata for serialization.

        Returns:
            dict: A dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel object.

        Returns:
            str: A string representation of the object.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
