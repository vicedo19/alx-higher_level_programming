#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""

def add_integer(a, b=98):
    """Return the addition of two numbers."""

    values = []
    for x in (a, b):
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(x))
    return sum(values)
