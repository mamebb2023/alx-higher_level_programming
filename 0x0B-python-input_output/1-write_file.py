#!/usr/bin/python3
""" File manipulations """


def write_file(filename="", text=""):
    """ Writes in to a file 

    Args:
        filename (str): the filename
        text (str): the text to write
    """
    cnt = 0
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)

    cnt  = len(text)

    return (cnt)
