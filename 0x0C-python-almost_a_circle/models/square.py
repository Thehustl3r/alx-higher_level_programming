#!/usr/bin/python3
""" File create by Mugisha Prosper"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ constructir"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def update(self, *args, **kwargs):
        """ Update function"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in (kwargs.items()):
                setattr(self, key, value)

    @property
    def size(self):
        """ size of function"""
        return self.width

    @size.setter
    def size(self, value):
        """ size of setter"""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ to_dictionary"""
        attribute = {"id": self.id,
                     "x": self.x,
                     "size": self.size,
                     "y": self.y}
        return attribute

    def __str__(self):
        """ str"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))
