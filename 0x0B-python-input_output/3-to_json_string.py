#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Created by Mugisha Prosper """
import json


def to_json_string(my_obj):
    """
    Returs a json string containg object's representation

    Argumens:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json format text
    """
    return json.dumps(my_obj)
