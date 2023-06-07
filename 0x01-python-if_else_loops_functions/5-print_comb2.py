#!/usr/bin/python3
for i in range(0, 100):
    if i < 10 or i == 99:
        print(0 if i < 10 else 99, end="" if i < 10 else "\n")
    if i != 99:
        print("{:d}, ".format(i), end="")
