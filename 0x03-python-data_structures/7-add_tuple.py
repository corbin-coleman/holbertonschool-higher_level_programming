#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            a_tuple = (tuple_a[0], 0)
        elif len(tuple_a) == 0:
            a_tuple = (0, 0)
    else:
        a_tuple = tuple_a
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            b_tuple = (tuple_b[0], 0)
        elif len(tuple_b) == 0:
            b_tuple = (0, 0)
    else:
        b_tuple = tuple_b
    new_tuple = (a_tuple[0] + b_tuple[0], a_tuple[1] + b_tuple[1])
    return (new_tuple)
