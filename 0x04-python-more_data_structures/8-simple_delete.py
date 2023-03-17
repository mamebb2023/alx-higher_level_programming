#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    d = a_dictionary
    if key not in d:
        return d
    del d[key]
    return (d)
