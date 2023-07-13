#!/usr/bin/python3
""" file created by Mugisha Prosper"""


def class_to_json(obj):
    """ function that convert all artribute to json"""
    class_json = {}
    class_obj = dir(obj)
    for attr in class_obj:
        if not attr.startswith("__") and not callable(getattr(obj, attr)):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, bool, int, str)):
                class_json[attr] = value
    return class_json
