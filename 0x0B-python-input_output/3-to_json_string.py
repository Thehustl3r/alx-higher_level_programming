#!/bin/usr/python3
import json
""" file created by Mugisha Prosper"""


def to_json_string(my_obj):
    """ function that converts to json"""
    return json.dumps(my_obj, sort_keys=True)
