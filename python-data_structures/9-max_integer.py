#!/usr/bin/python3
def max_integer(my_list=[]):
    m = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if i > m:
                m = i
    return m
