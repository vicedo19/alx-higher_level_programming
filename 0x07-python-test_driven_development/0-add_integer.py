#!/usr/bin/python3
"""function"""


def add_integer(a, b=98):
    """adding function"""

    values = []
    for x in (a, b):
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(x))
    return sum(values)
