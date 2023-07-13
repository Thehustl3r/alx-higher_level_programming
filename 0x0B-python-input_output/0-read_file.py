#!/usr/bin/python3

""" File created at by Muisha Prosper """


def read_file(filename=""):
    """ function that reads the file"""
    try:
        with open(filename) as file:
            text = file.read().rstrip()
            print(text)
    except PermissionError:
        print("Permission Denied")
    except FileNotFoundError:
        print("file doesn't exist")
