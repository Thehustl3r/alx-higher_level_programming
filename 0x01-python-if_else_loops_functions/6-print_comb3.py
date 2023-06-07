#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print(i, end="")
        print("{:d}".format(j), end="" if i != 8 else "\n")
        if i != 8:
            print(", ", end="")
