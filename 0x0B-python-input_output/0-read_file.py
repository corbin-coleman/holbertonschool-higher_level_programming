#!/usr/bin/python3
def read_file(filename=""):
    my_file = open(filename, 'r')
    print(my_file.read(), end="")
    my_file.close()
