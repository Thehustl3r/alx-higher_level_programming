#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list) - 1 or idx < 0:
        return (0)
    print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
