#!/usr/bin/python3
""" A module that describes a rectangle """


class Rectangle:
    """ Defines a rectangle """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """ Properties for width """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Properties for height """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif not value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value