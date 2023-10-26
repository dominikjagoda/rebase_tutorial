from calculator import add, mul, sub


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_sub():
    assert sub(5, 2) == 3
    assert sub(1, -1) == 2
    assert sub(0, 0) == 0


def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 4) == -4
    assert mul(0, 5) == 0
