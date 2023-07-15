#!/usr/bin/python3
""" Created on """


class MyList(list):
    """class MyLi that inherits from list"""
    def print_sorted(self):
        """Public instance method that prints sorted list"""
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
