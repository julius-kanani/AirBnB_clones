#!/usr/bin/python3
"""
file_storage module that supplies the FileStorage class.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage that serializes instances to a JSON file and deserializes
    JSON file to instances.

    Args
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

            self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file(path: __file_path).
        """
        base_model_objects = self.__objects.copy()

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
