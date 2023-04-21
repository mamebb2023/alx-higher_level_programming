#!/usr/bin/python3
""" A Square module """
from rectangle import Rectangle


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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints a string for the square """
        print("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))
