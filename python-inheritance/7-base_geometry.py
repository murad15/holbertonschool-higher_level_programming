#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Compute the area of the shape.

        Raises:
            Exception: Always raises as this method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
