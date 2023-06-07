#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        test = ord(str[i])
        if test > 96 and test < 123:
            for j in range(97, 123):
                if test == j:
                    test = test - 32
                    print("{:c}".format(test), end="")
                    break
        else:
            print("{:c}".format(test), end="" if i < len(str) else "\n")
