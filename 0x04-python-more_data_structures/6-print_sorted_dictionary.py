#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    d = a_dictionary
    [print("{}: {}".format(k, d[k])) for k in sorted(d)]
