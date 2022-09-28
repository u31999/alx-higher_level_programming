#!/usr/bin/python3
"""This module implements a custom list object"""


class MyList(list):
    """Custom list"""

    def print_sorted(self):
        """Print sorted list (ascending sort)"""
        print(sorted(self))
