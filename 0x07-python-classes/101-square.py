#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if type(i) is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if type(i) is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        spaces = ' ' * self.__position[0];
        square_print = '#'
        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print("{}{}".format(spaces, square_print * self.__size))
        else:
            print("")

    def __str__(self):
        if self.__size != 0:
            y_lines = '\n' * self.position[1]
            line = (' ' * self.__position[0]) + ('#' * self.__size)
            print_it = y_lines + ((line + '\n') * (self.__size + 1)) + line
        else:
            print_it = ""
        return (print_it)
