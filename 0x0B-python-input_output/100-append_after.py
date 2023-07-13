#!/usr/bin/python3
""" created by mugisha Prosper """


def append_after(filename="", search_string="", new_string=""):
    """ function that write new string at certain index in file """
    with open(filename, "r") as file:
        file_content = file.readlines()

    with open(filename, "w") as file:
        for line in file_content:
            file.write(line)
            if search_string in line:
                file.write(new_string)
