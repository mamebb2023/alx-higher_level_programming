#!/usr/bin/python3
""" File manipulations """


def write_file(filename="", text=""):
    """ Writes in to a file """
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(text)
    except FileNotFoundError:
        print("The file was not found")
