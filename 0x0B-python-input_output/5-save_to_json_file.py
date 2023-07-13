#!/usr/bin/python3
""" file created by Mugisha Prosper"""
import json


def save_to_json_file(my_obj, filename):
    """ function that save converted json"""
    with open(filename, "w") as file:
        json_obj = json.dumps(my_obj)
        file.write(json_obj)
        file.close()
