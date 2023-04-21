#!/usr/bin/python3
""" A Square module """
from rectangel import Rectangle


class Square(Rectangle):
    """ Defines a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Properties for a new square 

        Args:
            size (int): the size of the square
            x (int): the x position of the square
            y (int): the y postiton of the square
            id (any): a unique id for the square
        """
        super().__init__.width = size
        super().__init__.height = size
        super().__inti__(x)
        super().__inti__(y)
        super().__inti__(id)

    def __str__(self):
        """ Prints a string for the square """
        print("[Square] ({}) {}/{} - {}".format(id, x, y, size)
