#!/usr/bin/python3
"""Check if an object is an instance of a class or its subclass."""


class BaseGeometry:
    """Check if an object is an instance"""

    def area(self):
        raise Exception("area() is not implemented")
