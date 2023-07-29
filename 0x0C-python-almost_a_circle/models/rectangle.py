#!/usr/bin/python3
""" Created by Mugisha Prosper"""
from models.base import Base


class Rectangle(Base):
    """ Fuction that create rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor Function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x Setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """ Update args """
        if args:
            if len(args) >= 1:
                super().__init__(args[0])
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """ Area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display of the rectangle"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """ To dicionary """
        attributes = {'x': self.x,
                      'width': self.width,
                      'id': self.id,
                      'height': self.height,
                      'y': self.y}

        return attributes

    def __eq__(self, other):
        """Override the equality comparison to compare attributes."""
        if isinstance(other, Rectangle):
            return (
                self.id == other.id and
                self.width == other.width and
                self.height == other.height and
                self.x == other.x and
                self.y == other.y
            )
        return False

    def __str__(self):
        """ ovviride"""
        return ("[Rectangle] ({}) {}/{} - {}"
                "/{}".format(self.id, self.x, self.y, self.width, self.height))
