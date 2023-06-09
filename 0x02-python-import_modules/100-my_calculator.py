#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    ac = len(argv) - 1
    if ac < 4:
        print("{} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+" or argv[2] == "-" or argv[2] == "*" or argv[2] == "/":
            if argv[2] == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif argv[2] == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif argv[2] == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
