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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
