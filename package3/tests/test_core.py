def test_power():
    assert 2 ** 3 == 8
    assert 5 ** 0 == 1
    assert 3**-2 == 1/9
    
def test_root():
    assert 9 ** 0.5 == 3
    assert 16 ** 0.25 == 2
    assert 27 ** (1/3) == 3
