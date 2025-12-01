#!/usr/bin/python3
def print_last_digit(number):
    try:
        last = abs(int(number)) % 10
        print(last)
        return last
    except (ValueError, TypeError):
        print("Input must be a number")
        return None
