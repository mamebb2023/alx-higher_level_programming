#!/usr/bin/python3

""" Square Module

Containes a class that defiens a square

"""


class Square:

    """ Defines a square

    Args:
        size (int): the size of the square
    """
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    """ Calculates the area of the square"""
    def area(self):
        return self.__size * self.__size

    """ Prints the square in '#' """
    def my_print(self):
        if self.__size == 0:
            print()

        [print("") for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for x in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")

    """ Gets the value of position """
    @property
    def position(self):
        return self.__position

    """ Sets the value of the position

    Args:
        position (int): position of the square
    """
    @position.setter
     def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


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
