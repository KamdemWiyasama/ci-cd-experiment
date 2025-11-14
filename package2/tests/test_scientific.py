from package2.tests import scientific

ITERATIONS = 1_000_000

def test_power():
    for _ in range(ITERATIONS):
        assert test_scientific.power(2, 3) == 8

def test_square_root():
    for _ in range(ITERATIONS):
        assert test_scientific.square_root(16) == 4

