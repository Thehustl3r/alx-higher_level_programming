#!/usr/bin/python3


def safe_print_integer(value):
    """
    prints a list onything, but only prints the integers
    Returns the amot of integers printed
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
