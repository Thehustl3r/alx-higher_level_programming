#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_array = []
    neww_array = []
    for i in set_1:
        for j in set_2:
            if i == j:
                new_array.append(i)
    for i in set_1:
        for test in new_array:
            if i != test:
                neww_array.append(i)
    for j in set_2:
        for test in new_array:
            if j != test:
                neww_array.append(j)

    return neww_array
