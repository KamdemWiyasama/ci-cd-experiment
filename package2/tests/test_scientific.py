from package2.tests import test_scientific

ITERATIONS = 1_000_000

def power():
    for _ in range(ITERATIONS):
        assert test_scientific.power(2, 3) == 8

def square_root():
    for _ in range(ITERATIONS):
        assert test_scientific.square_root(16) == 4

