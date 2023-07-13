#!/bin/usr/python3
import json
""" file created by Mugisha Prosper"""


def load_from_json_file(filename):
    """ function that converts json to string from file"""
    with open(filename, "r") as file:
        json_obj = file.read()
        file.close()
        parsed_obj = json.loads(json_obj)
        return parsed_obj
