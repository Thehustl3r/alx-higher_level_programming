#!/usr/bin/python3
""" Created by Mugisha Prosper"""
import unittest
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """ Class that used to test"""

    def setUp(self):
        self.r1 = Rectangle(4, 5)
        self.r2 = Rectangle(2, 3)
        self.r3 = Rectangle(3, 4, 1, 2, 10)

    def tearDown(self):
        pass

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)

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

        # Test update method for r1
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


if __name__ == "__main__":
    unittest.main()
