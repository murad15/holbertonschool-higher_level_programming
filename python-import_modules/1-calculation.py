#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    "{} + {} = {}".format(a, b, add(a, b))
    "{} - {} = {}".format(a, b, sub(a, b))
    "{} * {} = {}".format(a, b, mul(a, b))
    "{} / {} = {}".format(a, b, div(a, b))



