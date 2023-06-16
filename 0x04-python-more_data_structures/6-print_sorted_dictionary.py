#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    for key, value in sorted_dict.items():
        print(key, ':', value)
