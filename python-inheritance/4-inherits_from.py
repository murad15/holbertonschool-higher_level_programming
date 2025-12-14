#!/usr/bin/python3
"""Check if an object is an instance of a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class its from a_class."""
    return type(obj) is not a_class and isinstance(obj, a_class)
