#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    prints a lit of anyhing, but only prints the integers
    Return the ount of integers printed
    """
    j = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except (ValueError, TypeError):
            continue
    print()
    return j
