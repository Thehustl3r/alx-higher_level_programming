#!/usr/bin/python3

""" file created by Mugisha Prosper """


def write_file(filename="", text=""):
    """ function that write in the file"""
    n = len(text)
    with open(filename, "w") as file:
        file.write(text)
        file.close()
        return n

