#!/usr/bin/python3
""" Create by Mugisha Prosper"""
import json


class Base:
    """ Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ function that save converted json"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            json_obj = cls.to_json_string(list_dicts)
            file.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("invalid class name")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ function that converts json to string from file"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                json_obj = file.read()
        except FileNotFoundError:
            return []
        list_dicts = json.loads(json_obj)
        instance = [cls.create(**dict_obj) for dict_obj in list_dicts]
        return instance
