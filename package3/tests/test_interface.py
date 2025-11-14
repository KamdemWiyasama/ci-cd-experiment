# package3/tests/test_interface.py

from package1 import core
from package2 import scientific

ITERATIONS = 1_000_000  # scale workload to make pipeline timing visible

def test_interface_add():
    for _ in range(ITERATIONS):
        assert core.add(10, 5) == 15

def test_interface_subtract():
    for _ in range(ITERATIONS):
        assert core.subtract(10, 5) == 5

def test_interface_multiply():
    for _ in range(ITERATIONS):
        assert core.multiply(3, 4) == 12

def test_interface_divide():
    for _ in range(ITERATIONS):
        assert core.divide(12, 4) == 3

def test_interface_power():
    for _ in range(ITERATIONS):
        assert scientific.power(2, 5) == 32

def test_interface_square_root():
    for _ in range(ITERATIONS):
        assert scientific.square_root(49) == 7