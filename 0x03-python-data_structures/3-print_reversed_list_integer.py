#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    if my_list != None:
        my_list.reverse()
        for ele in my_list:
            print("{:d}".format(ele))
