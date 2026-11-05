from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_sub():
    assert subtract(10, 7) == 3

def test_multiply():
    assert multiply(12, 4) == 48

def test_divide_uneven():
    a, b = 5, 2
    result = divide(a, b)
    assert result == 2.5