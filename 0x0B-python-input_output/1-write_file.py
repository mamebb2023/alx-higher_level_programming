#!/usr/bin/python3
""" File manipulations """


def write_file(filename="", text=""):
    """ Writes in to a file """
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(text)
