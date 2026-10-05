#! python

import pytest
import math
from calculator import add, subtract, multiply, divide, power

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_with_zero():
    assert add(0, 5) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(3, 7) == -4

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_multiply_positive():
    assert multiply(3, 7) == 21

def test_multiply_by_zero():
    assert multiply(100, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_divide_positive():
    assert divide(8, 2) == 4

def test_divide_floats():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="ошибка"):
        divide(5, 0)

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (10, 20, 30),
    (-5, 5, 0),
    (0, 0, 0),
    (1.1, 2.2, pytest.approx(3.3)),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (7, 2, 3.5),
    (-10, 2, -5),
])
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])   