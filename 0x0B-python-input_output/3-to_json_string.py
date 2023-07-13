#!/bin/usr/python3
# -*- coding: utf-8 -*-
""" file created by Mugisha Prosper"""
import json


def to_json_string(my_obj):
    """
    function that converts to json

    Argruments:
        my_obj (str): a list needed to converted to json
    Return:
        A json format text
    """
    return json.dumps(my_obj, sort_keys=True)
