#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    ava = 0
    size = 0
    for x in my_list:
        ava += (x[0] * x[1])
        size += x[1]
    return (ava / size)
