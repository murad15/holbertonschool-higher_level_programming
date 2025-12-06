#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dict = a_dictionary.copy()
    for i in b_dict.keys():
        b_dict[i] = b_dict[i]*2
    return b_dict
