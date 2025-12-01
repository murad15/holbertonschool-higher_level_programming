#!/usr/bin/python3
def print_last_digit(number):
    last = abs(int(number)) % 10
    print(last)
    return last
