#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        test = str[i]
        for j in range(97, 123):
            if test == j:
                test = test - 32
                break
        str[i] = chr(test)
    print("{}".format(str))