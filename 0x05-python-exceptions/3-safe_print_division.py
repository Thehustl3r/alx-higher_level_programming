#!/usr/bin/python3


def safe_print_division(a, b):
    """
    dividestwo integers and prints the result
    catchesdivide by zero exception
    """
    try:
        r = a / b
    except:
        r = None
    finally:
        print("Inside result: {}".format(r))
    return r
