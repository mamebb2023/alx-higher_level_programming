#!/usr/bin/python3
""" Adds intigers """


def add(a, b=98):
    """ Adds a and b

    Args:
        a (int): the first int
        b (int): the second int
    Raises:
        TypeError: a or b are not numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
