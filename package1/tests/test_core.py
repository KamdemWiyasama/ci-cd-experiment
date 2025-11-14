from package1 import core

ITERATIONS = 1_000_000  

def test_addition():
    for _ in range(ITERATIONS):
        assert core.add(1, 1) == 2

def test_subtraction():
    for _ in range(ITERATIONS):
        assert core.subtract(5, 3) == 2

def test_multiplication():
    for _ in range(ITERATIONS):
        assert core.multiply(2, 3) == 6

def test_division():
    for _ in range(ITERATIONS):
        assert core.divide(6, 2) == 3

