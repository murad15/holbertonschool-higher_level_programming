#!/usr/bin/python3
"""Defines a function that tance of a class."""


def is_same_class(obj, a_class):
    """Check if `obj` is exactly an instance of `a_class`.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True i, False otherwise.
    """
    return type(obj) is a_class
