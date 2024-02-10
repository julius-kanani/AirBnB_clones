#!/usr/bin/python3
"""
file_storage module that supplies the FileStorage class.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
     Defines the File storage class, that serializes instances to a JSON
     file and deserializes JSON file to instances

    Attributes:
        __file_path (str): path to JSON File (ex: file.json).
        __objects: (dictionary): Empty, but will store all objects by
            <class name>.id (ex: to store a BaseModel object with
            d=12121212, the key will be BaseModel.12121212)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = "{:s}{:s}{:s}".format(
                type(obj).__name__, ".", obj.id)

            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file(path: __file_path).
        """
        objects_dictionary = self.__objects.copy()
        for key, obj in objects_dictionary.items():
            object_dictionary[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(base_model_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __ objects (only if the JSON file
        (__file_path) exists; otherwise. do nothing. if the file doesn't
        exist no file should be raised.
        """

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                base_model_objs = json.load(file)
                for key, value in base_model_objs.items():
                    obj = BaseModel(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
