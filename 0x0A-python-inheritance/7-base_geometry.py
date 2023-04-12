#!/usr/bin/python3
""" Defines an empty class BaseGeometry """


class BaseGeometry:
    """ Defines BaseGeometry"""

    def area(self):
        """ Raises an Exeption """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value

        Args:
            name (str): integer
            value (int): value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
