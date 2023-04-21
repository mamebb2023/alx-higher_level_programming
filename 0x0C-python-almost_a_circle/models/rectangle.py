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

    """ getter/setter for y """
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

    def area(self):
        """ Finds the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Display the rectangle """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """ Assign new values for the coordinate and sides

        Args:
            *args (ints): the new values
                        1st argument should be the id attribute
                        2nd argument = the width attribute
                        3rd argument = the height attribute
                        4th argument = the x attribute
                        5th argument = the y attribute
        """
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs is not None:
            for key, value, in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Print the coordinate and the sides of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
