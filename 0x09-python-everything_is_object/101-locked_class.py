#!/usr/bin/python3
"""
This is a module that contains a class that avoids
dynamically created attributes.
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
