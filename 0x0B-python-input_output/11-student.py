#!/usr/bin/python3
""" file created by Mugisha Prosper"""


class Student:
    """ a class of students"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function that convert all artribute to json"""
        if attrs is None:
            attrs = list(self.__dict__)
        class_json = {}
        for attr in attrs:
            if attr not in self.__dict__:
                continue
            value = getattr(self, attr)
            class_json[attr] = value
        return class_json

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
