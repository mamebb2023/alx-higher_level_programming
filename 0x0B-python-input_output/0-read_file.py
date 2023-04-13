#!/usr/bin/python3
""" Opening a file """


def read_file(filename=""):
    """ Opens and prints the contents of the file """
    with open(filename, encoding="utf-8") as o_file:
        print(o_file.read(), end="")
