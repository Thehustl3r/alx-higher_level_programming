#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Mugisha Prosper
"""


class Square:
    """Class Square thathas attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int'): A private instance size
        """
        self.__size = size
