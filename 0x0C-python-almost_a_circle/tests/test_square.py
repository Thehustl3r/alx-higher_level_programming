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

    def tearDown(self):
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


if __name__ == "__main__":
    unittest.main()
