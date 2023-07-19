#!/usr/bin/python3
""" Created by Mugisha Prosper"""
from models.base import Base


class Rectangle(Base):
    """ Fuction that create rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def x(self):
        return self.__x

    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    def y(self):
        return self.__y

    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
