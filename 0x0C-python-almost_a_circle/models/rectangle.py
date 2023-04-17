#!/usr/bin/python3
""" A Module for a Rectangle """
Base = __import__('model/base').Base


class Rectangle(Base):
    """ Defines Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initislize a new rectangle

        Args:
            width (int): The width
            height (int): The height
            x (int): The x coordinate
            y (int): The y coordinate
            id (int): The identity of the rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__.id = id

    """ getter/setter for width """
    @properties
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    """ getter/setter for height """
    @properties
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    """ getter/setter for x """
    @properties
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    """ getter/setter for y"""
    @properties
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
