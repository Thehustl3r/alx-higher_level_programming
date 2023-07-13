#!/usr/bin/python3
""" created by Mugisha Prosper"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


av = sys.argv
filename = "add_item.json"
try:
    lists = load_from_json_file(filename)
except FileNotFoundError:
    lists = []
if len(av) > 1:
    for i in range(1, len(av)):
        lists.append(av[i])
save_to_json_file(lists, filename)
