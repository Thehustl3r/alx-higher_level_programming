#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = []
    for i in my_list:
        if i == search:
            i = replace
        new_matrix.append(i)

    return new_matrix
