#!/usr/bin/python3
for i in range(0, 8):
    for j in range(1, 9):
        if j > i:
            print("{:d}{:d}, ".format(i, j), end="")
print("{:d}".format(89))
