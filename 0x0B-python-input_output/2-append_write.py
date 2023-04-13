#!/usr/bin/python3
""" File manipulations """


def append_write(filename="", text=""):
    """ Appends a text to a file

    Args:
        filename (str): the file name
        text (str): the text to append
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
