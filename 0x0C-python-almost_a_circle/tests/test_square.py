#!/usr/bin/python3
""" Created by Mugisha Prosper"""
import unittest
from models.square import Square
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """ Class that used to test"""

    def setUp(self):
        self.s1 = Square(4)
        self.s2 = Square(3, 1, 2, 10)
        self.s3 = Square(2, 1, 2, 1)
        self.s4 = Square(1, 1, 1, 1)

    def tearDown(self):
        Square._Base__nb_objects = 0
        pass

    def test_area(self):
        self.assertEqual(self.s1.area(), 16)

    def test_display(self):
        expected_output = "####\n" \
                          "####\n" \
                          "####\n" \
                          "####\n"
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            self.s1.display()
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        expected_string = "[Square] (10) 1/2 - 3"
        self.assertEqual(str(self.s2), expected_string)

    def test_invalid_side_type(self):
        with self.assertRaises(TypeError):
            s = Square("1")

        with self.assertRaises(TypeError):
            s = Square(1, "2")

        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    def test_invalid_side_value(self):
        with self.assertRaises(ValueError):
            s = Square(-1)

        with self.assertRaises(ValueError):
            s = Square(1, -2)

        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_zero_side_value(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_to_dictionary(self):
        s1_dict = self.s1.to_dictionary()
        expected_s1_dict = {'id': 46, 'size': 4, 'x': 0, 'y': 0}
        self.assertDictEqual(s1_dict, expected_s1_dict)

        s3_dict = self.s2.to_dictionary()
        expected_s3_dict = {'id': 10, 'size': 3, 'x': 1, 'y': 2}
        self.assertDictEqual(s3_dict, expected_s3_dict)

        self.s1.update(10)
        self.assertEqual(self.s1.id, 10)

        self.s2.update(10, 5)
        self.assertEqual(self.s2.id, 10)
        self.assertEqual(self.s2.size, 5)

        self.s3.update(10, 5, 3)
        self.assertEqual(self.s3.id, 10)
        self.assertEqual(self.s3.size, 5)
        self.assertEqual(self.s3.x, 3)

        self.s4.update(10, 5, 3, 2)
        self.assertEqual(self.s4.id, 10)
        self.assertEqual(self.s4.size, 5)
        self.assertEqual(self.s4.x, 3)
        self.assertEqual(self.s4.y, 2)

        self.s1.update(**{'id': 89})
        self.assertEqual(self.s1.id, 89)

        self.s2.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.s2.id, 89)
        self.assertEqual(self.s2.size, 1)

        self.s3.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(self.s3.id, 89)
        self.assertEqual(self.s3.size, 1)
        self.assertEqual(self.s3.x, 2)

        self.s4.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(self.s4.id, 89)
        self.assertEqual(self.s4.size, 1)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s4.y, 3)

    def test_create(self):
        # Test create with id only
        s1 = Square.create(**{'id': 89})
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        # Test create with id and size
        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.id, 89)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

        # Test create with id, size, and x
        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertIsInstance(s3, Square)
        self.assertEqual(s3.id, 89)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 0)

        # Test create with all attributes
        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertIsInstance(s4, Square)
        self.assertEqual(s4.id, 89)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)

    def test_save_to_file(self):
        Square._Base__nb_objects = 0

        # Test save an empty list
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

        # Test save a list containing a single Square instance
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            data = file.read()
            expected_data = '[{"id": 44, "x": 0, "size": 1, "y": 0}]'
            self.assertEqual(data, expected_data)

        # Test save None
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")


if __name__ == "__main__":
    unittest.main()
