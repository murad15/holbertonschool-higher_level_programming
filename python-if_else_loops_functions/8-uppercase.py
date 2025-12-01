#!/usr/bin/python3
def uppercase(s):
    res = ""
    for c in s:
        if 'a' <= c <= 'z':
            res += chr(ord(c) - 32)
        else:
            res += c
    print("{}".format(res))
