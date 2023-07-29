#!/usr/bin/python3
""" Created by Mugisha Prosper"""
import unittest
from models.rectangle import Rectangle
import io
import os
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """ Class that used to test"""

    def setUp(self):
        self.r1 = Rectangle(4, 5)
        self.r2 = Rectangle(2, 3)
        self.r3 = Rectangle(3, 4, 1, 2, 10)

    def tearDown(self):
        Rectangle._Base__nb_objects = 0

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_display(self):
        expected_output = "##\n" \
                          "##\n" \
                          "##\n"
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            self.r2.display()
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        expected_string = "[Rectangle] (10) 1/2 - 3/4"
        self.assertEqual(str(self.r3), expected_string)

        self.r1.update(10)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 0/0 - 4/5")
        self.r1.update(10, 6)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 0/0 - 6/5")
        self.r1.update(10, 6, 7)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 0/0 - 6/7")
        self.r1.update(10, 6, 7, 8)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 8/0 - 6/7")
        self.r1.update(y=9, x=10, width=11, id=12)
        self.assertEqual(str(self.r1), "[Rectangle] (12) 10/9 - 11/7")

        self.r3.update(size=7)
        self.assertEqual(str(self.r3), "[Rectangle] (10) 1/2 - 3/4")
        self.r3.update(size=8, x=9)
        self.assertEqual(str(self.r3), "[Rectangle] (10) 9/2 - 3/4")
        self.r3.update(y=10, x=11, width=12)
        self.assertEqual(str(self.r3), "[Rectangle] (10) 11/10 - 12/4")

        # Test create with id only
        r = Rectangle.create(**{'id': 89})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        # Test create with id and width
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        """ Test create with id, width, and height """
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        """Test create with all attributes"""
        r = Rectangle.create(**{'id': 89, 'width': 1,
                                'height': 2, 'x': 3, 'y': 4})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_save_to_file(self):
        Rectangle._Base__nb_objects = 0

        # Test save an empty list
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

        # Test save a list containing a single Rectangle instance
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            data = file.read()
            expected_data = '[{"x": 0, "width": 1,' \
                            ' "id": 21, "height": 2, "y": 0}]'
            self.assertEqual(data, expected_data)

        # Test save None
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_load_from_file_when_file_doesnt_exist(self):
        # Make sure the file doesn't exist
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        # Load from file when it doesn't exist
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
