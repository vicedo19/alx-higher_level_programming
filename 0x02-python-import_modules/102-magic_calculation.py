#!usr/bin/python3
def magic_calculation(a, b):
    from calculator_1 import add, sub
    if (a < b):
        c = add(a, b)
    for i in range(90):
        if i == 89:
            c = add(c, i)
        return c
    return sub(a, b)
