from package2 import scientific

ITERATIONS = 1_000_000

def test_power():
    for _ in range(ITERATIONS):
        assert scientific.power(2, 3) == 8

def test_square_root():
    for _ in range(ITERATIONS):
        assert scientific.square_root(16) == 4

