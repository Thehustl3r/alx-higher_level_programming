#!/usr/bin/python3
""" Created by mugisha prosper"""


def inherits_from(obj, a_class):
    """ The function the check wheathe instance in certain class """
    obj_class = type(obj)
    if not isinstance(a_class, type):
        return False
    if issubclass(obj_class, a_class) and obj_class is not a_class:
        return True
    return False
