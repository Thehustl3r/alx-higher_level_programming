#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0
    flag = 0
    for a, i in enumerate(my_list):
        flag = 0
        for b, j in enumerate(my_list):
            if i == j and a != b:
                flag = 1
                break
        if flag == 0:
            summ = summ + i
    return summ
