#!/usr/bin/python3
""" file created by Mugisha Prosper"""


class Student:
    """ a class of students"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function that convert all artribute to json"""
        class_json = {}
        class_obj = dir(self)
        for attr in class_obj:
            if not attr.startswith("__") and not callable(getattr(self, attr)):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, bool, int, str)):
                    class_json[attr] = value
        return class_json
