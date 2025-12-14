#!/usr/bin/python3
"""Function that appends a str and returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends text to a -8 file and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
