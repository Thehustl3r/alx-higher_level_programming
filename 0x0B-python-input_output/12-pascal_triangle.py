#!/usr/bin/python3
""" created by mugisha prosper"""


def pascal_triangle(n):
    """ Fuction that prints the pascals triangle"""
    pascal_list = []
    sub_list = []
    prev_list = []
    for i in range(0, n):
        sub_list = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                sub_list.append(1)
            else:
                tmp = prev_list[j - 1] + prev_list[j]
                sub_list.append(tmp)
        pascal_list.append(sub_list)
        prev_list = sub_list[:]
    return pascal_list
