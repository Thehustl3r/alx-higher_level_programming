#!/usr/bin/python3
""" File create by Mugisha Prosper"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def update(self, *args, **kwargs):
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in (kwargs.items()):
                setattr(self, key, value)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        attribute = {"id": self.id,
                     "x": self.x,
                     "size": self.size,
                     "y": self.y}
        return attribute

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))
