#!/usr/bin/python3
"""Inherit from list"""


class MyList(list):
    """Inheritance from list"""

    def print_sorted(self):
        """Print something here"""
        print(sorted(self))
