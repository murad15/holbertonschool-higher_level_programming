#!/usr/bin/python3
"""Defines a function that tance of a class."""


def is_same_class(obj, a_class):
    """Check if `obj` is exactly an instance of the class a_class"""

    return type(obj) is a_class
