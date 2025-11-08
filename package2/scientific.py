import math

def power(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)
