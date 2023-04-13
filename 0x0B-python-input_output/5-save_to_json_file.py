#!/usr/bin/python3
""" Writes an object file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a file using
    json representation 

    Args:
        my_obj (dict): the object file
        filename (str): the file name
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
