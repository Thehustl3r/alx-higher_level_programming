#!/usr/bin/python3
""" Created by mugisha prosper"""


def is_same_class(obj, a_class):
    """ The function the check wheathe instance in certain class """
    if not isinstance(a_class, type):
        return False
    return (type(obj) is a_class)
