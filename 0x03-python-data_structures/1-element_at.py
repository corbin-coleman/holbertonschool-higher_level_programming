#!/usr/bin/python3
def element_at(my_list, idx):
    my_idx = 0
    for ele in my_list:
        if my_idx == idx:
            return (ele)
        my_idx += 1
    return (None)
