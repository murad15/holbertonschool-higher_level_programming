#!/usr/bin/python3
"""Function that returns escription for JSON serialization of an object"""


def class_to_json(obj):
    """Return the dictionary epresentation of obj's attributes"""
    return obj.__dict__.copy()
