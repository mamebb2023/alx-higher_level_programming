#!/usr/bin/bash
""" Writes an object file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a file using
    json representation 

    Args:
        my_obj (dict): the object file
        filename (str): the file name
    """
    dump = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(dump)
