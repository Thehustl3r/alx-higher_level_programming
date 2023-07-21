#!/usr/bin/python3
""" Created by Mugisha Prosper"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Class that used to test"""

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-2).id, -2)

    def test_to_json_string(self):
        list_dicts = [{'id': 1, 'width': 2, 'height': 3},
                      {'id': 4, 'width': 5, 'height': 6}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, '[{"id": 1, "width": 2, "height": 3},'
                                      ' {"id": 4, "width": 5, "height": 6}]')

        empty_list = []
        json_string_empty = Base.to_json_string(empty_list)
        self.assertEqual(json_string_empty, '[]')

        json_string_none = Base.to_json_string(None)
        self.assertEqual(json_string_none, '[]')

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 2, "height": 3},' \
                        '{"id": 4, "width": 5, "height": 6}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_dicts, [{'id': 1, 'width': 2, 'height': 3},
                                      {'id': 4, 'width': 5, 'height': 6}])

        json_string_empty = '[]'
        empty_list = Base.from_json_string(json_string_empty)
        self.assertEqual(empty_list, [])


if __name__ == "__main__":
    unittest.main()
