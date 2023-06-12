#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    tuple_b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tuple_c)
