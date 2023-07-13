#!/usr/bin/python3

""" File created at by Muisha Prosper """


def read_file(filename=""):
    """ function that reads the file"""
    with open(filename) as file:
        print(file.read(), end="")
