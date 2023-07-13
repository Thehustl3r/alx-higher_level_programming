#!/usr/bin/python3

""" file created by Mugisha Prosper """


def append_write(filename="", text=""):
    """ function that write in the file"""
    n = len(text)
    with open(filename, "a") as file:
        file.write(text)
        file.close()
        return n
