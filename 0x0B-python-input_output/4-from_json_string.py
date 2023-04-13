#!/usr/bin/python3
""" JSON representation """
import json


def from_json_string(my_str):
    """ Returns the python data structure
    from json representation """
    return json.loads(my_str)
