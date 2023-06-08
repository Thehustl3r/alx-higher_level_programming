#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    summ = 0
    num = 0
    if argc == 0:
        print("{}".format(argc))
    else:
        for i in range(1, argc + 1):
            num = int(argv[i])
            summ = summ + num
        print("{}".format(summ))
