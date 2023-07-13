#!/bin/usr/python3
import json
""" file created by Mugisha Prosper"""


def save_to_json_file(my_obj, filename):
    """ function that save converted json"""
    with open(filename, "w") as file:
        json_obj = json.dumps(my_obj)
        file.write(json_obj)
        file.close()

