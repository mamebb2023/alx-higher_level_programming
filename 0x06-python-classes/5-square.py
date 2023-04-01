#!/usr/bin/python3

""" Square Module

Containes a class that defiens a square

"""


class Square:

    """ Defines a square

    Args:
        size (int): the size of the square
    """
    def __init__(self, size=0):
        self.__size = size

    """ Calculates the area of the square"""
    def area(self):
        return self.__size * self.__size

    """ Prints the square in '#' """
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")

    """ Gets the value of size """
    @property
    def size(self):
        return self.__size

    """ Sets a value to size

    Args:
        size (int): the size of the square
    """
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
