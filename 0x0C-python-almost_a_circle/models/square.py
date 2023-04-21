#!/usr/bin/python3
""" A Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Properties for a new square

        Args:
            size (int): the size of the square
            x (int): the x position of the square
            y (int): the y postiton of the square
            id (int): a unique id for the square
        """
        super().__init__(size, size, x, y, id)

    """ Getter/Setter methods for the square """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the attributes with the given values

        Args:
            args (int): the number of arguments
            kwargs (dict): array of the arguments
        """
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Prints a string for the square """
        return ("[Square] ({}) {}/{} - {}".format(
                                        self.id,
                                        self.x,
                                        self.y,
                                        self.width))
