#!/usr/bin/python3
""" Checkes if the object is exactly an instance of 
object class """


def is_same_class(obj, a_class):
    """ Return True if the object is exactly an instance of
    object class, else False

    Args:
        obj (any): the object to check
        a_class (type): the class to match the obj

    Return:
        'True' if the object is an instance of object class
        else 'False'
    """
    if type(obj) == a_class:
        return True
    return False
