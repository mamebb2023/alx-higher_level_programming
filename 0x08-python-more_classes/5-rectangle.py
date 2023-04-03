#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Represent a rectangle """

    def __init__(self, width=0, height=0):
        """ Defiens a new Rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Properties of the width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Properties of the height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return the perimeter """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """ Prints the rectangle

        Show the rectangle with '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        x = []
        for i in range(self.__height):
            [x.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                x.append("\n")
        return ("".join(x))

    def __repr__(self):
        """ Return a string representation of the rectangle """
        x = "Rectangle(" + str(self.__width)
        x += ", " + str(self.__height) + ")"
        return (x)

    def __del__(self):
        """ Prints a message when deletetion """
         print("Bye rectangle...")
