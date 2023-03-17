#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    d = a_dictionary
    new_list = {k: d[k]*2 for k in d}
    return (new_list)
