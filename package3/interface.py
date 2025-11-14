from package1 import core
from package2 import scientific

ITERATIONS = 1_000_000

def test_interface_add():
    for _ in range(ITERATIONS):
        assert core.add(10, 5) == 15

def test_interface_pow():
    for _ in range(ITERATIONS):
        assert scientific.power(3, 2) == 9
