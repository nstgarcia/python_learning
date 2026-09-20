import angle

def test_twelve():
    assert angle.between(12, 00) == 0

def test_three():
    assert angle.between(3, 00) == 90
