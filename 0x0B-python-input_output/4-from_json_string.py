#!/bin/usr/python3
import json
""" file created by Mugisha Prosper"""


def from_json_string(my_str):
    """ function that converts json to string"""
    parsed_obj = json.loads(my_str)
    if isinstance(parsed_obj, dict):
        sorted_obj = dict(sorted(parsed_obj.items()))
    if isinstance(parsed_obj, list):
        sorted_obj = sorted(parsed_obj)
    return sorted_obj
