#!/bin/usr/python3

class Square:
    __size = 3
    __dict__ = {'_square__size': __size}

    def __init__(self, __size):
        self.__size = __size
        Square.__size = self.__size
