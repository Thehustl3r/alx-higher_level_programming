#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Prosper Mugisha
"""


class Square:
    """Class Square thatas attributes. Instantiation with size

    Attributes:
        size (int): The ize of the square
    """

    def __init__(self, size=0):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int', optional): A private instance size

        Raises:
            TypeError: Exceptio if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            The square are
        """
        return self.__size ** 2
