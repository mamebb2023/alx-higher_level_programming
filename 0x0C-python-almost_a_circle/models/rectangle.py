#!/usr/bin/python3
""" A Module for a Rectangle """
from models.base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """ getter/setter for width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ getter/setter for height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ getter/setter for x """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ getter/setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
