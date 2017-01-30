#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, val2):
        return self - val2 is not 0

    def __ne__(self, val2):
        return self - val2 is 0

