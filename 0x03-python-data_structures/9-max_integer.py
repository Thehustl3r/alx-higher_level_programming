#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    tmp = 0
    for i in my_list:
        if tmp <= i:
            tmp = i
    if tmp == 0:
        return
    return tmp
