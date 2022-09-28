#!/usr/bin/python3
"""
This module implements a custom list object
"""


class MyList(list):
    """Subclass of list
    """
    def __init__(self):
        """Intilization"""
        super().__init__()
        
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
