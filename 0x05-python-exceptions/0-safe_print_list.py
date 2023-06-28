#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    prints a lis of anything, but only prints the integers
    Returns the aount of integers printed
    """
    j = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except:
            continue
    print()
    return j
