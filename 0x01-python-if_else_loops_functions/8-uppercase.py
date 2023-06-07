#!/usr/bin/python3
def uppercase(str):
    newstring = []
    for i in range(len(str)):
        test = ord(str[i])
        for j in range(97, 123):
            if test == j:
                test = test - 32
                print("{:c}".format(test), end="")
                break
        print("{:c}".format(test), end="")
        newstring.append(chr(test))
