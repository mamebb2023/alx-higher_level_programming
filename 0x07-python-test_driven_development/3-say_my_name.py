#!/usr/bin/python3
""" Print the persons name """


def say_my_name(first_name, last_name=""):
    """ Print the persons name

    Args:
        first_name (str): first name of the person
        last_name (str): last name of the person
    Raise:
        TypeError: if either of the names are not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
