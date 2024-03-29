#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """ Represent a rectangle using BaseGeometry """

    def __init__(self, width, height):
        """ Intialize a new Rectangle
        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
