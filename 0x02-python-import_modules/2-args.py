#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{:d} ".format(len(sys.argv) - 1), end="")
    if len(sys.argv) - 1 == 0:
        print("argument.")
    else:
        print("arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
