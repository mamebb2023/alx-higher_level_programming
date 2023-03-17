#!/usr/bin/python3

def best_score(a_dictionary):
    d = a_dictionary
    if not isinstance(d, dict) or len(d) == 0:
        return None

    key = list(d.keys())[0]
    val = d[key]

    for k, v in d.items():
        if v > val:
            val = v
            key = k

    return (key)
