#!/usr/bin/python3
"""Student class with JSON serialization and deserialization"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of a Student instance.
        If attrs is a list of strings, only include those attributes.
        Otherwise, include all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using a dictionary (json).
        """
        for key, value in json.items():
            setattr(self, key, value)
