from calculator import add, multiply, subtract, square_root


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_sub():
    assert subtract(5, 2) == 3
    assert subtract(1, -1) == 2
    assert subtract(0, 0) == 0


def test_mul():
    assert multiply(2, 3) == 6
    assert multiply(-1, 4) == -4
    assert multiply(0, 5) == 0


def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(25) == 5


def test_square_root2():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(25) == 5
