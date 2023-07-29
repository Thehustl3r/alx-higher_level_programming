#!/usr/bin/python3
""" Create by Mugisha Prosper"""
import json
import csv
import turtle


class Base:
    """ Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ function that save converted json"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            json_obj = cls.to_json_string(list_dicts)
            file.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("invalid class name")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ function that converts json to string from file"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                json_obj = file.read()
        except FileNotFoundError:
            return []
        list_dicts = json.loads(json_obj)
        instance = [cls.create(**dict_obj) for dict_obj in list_dicts]
        return instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to filr csv function"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id,
                                         obj.width,
                                         obj.height,
                                         obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ load from file from csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, newline='') as file:
                reader = csv.reader(file)
                data = [list(map(int, row)) for row in reader]
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                return [cls(**dict(zip(fields, row))) for row in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw function"""
        screen = turtle.Screen()
        screen.setup(800, 600)
        t = turtle.Turtle()
        t.speed(1)

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)

        turtle.done()
