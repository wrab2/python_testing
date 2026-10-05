#! python

import pytest
from calculator import add, subtract, multiply, divide, power


@pytest.fixture
def numbers():
    return 10, 5


@pytest.fixture
def zero():
    return 0


def test_add_positive(numbers):
    a, b = numbers
    assert add(a, b) == 15


def test_add_negative():
    assert add(-2, -3) == -5


def test_subtract_positive(numbers):
    a, b = numbers
    assert subtract(a, b) == 5


def test_subtract_negative_result():
    assert subtract(3, 7) == -4


def test_multiply_positive():
    assert multiply(3, 7) == 21


def test_multiply_by_zero(numbers, zero):
    a, _ = numbers
    assert multiply(a, zero) == 0


def test_divide_positive(numbers):
    a, b = numbers
    assert divide(a, b) == 2


def test_divide_floats():
    assert divide(5, 2) == 2.5


def test_divide_by_zero(numbers, zero):
    a, _ = numbers
    with pytest.raises(ValueError, match="ошибка"):
        divide(a, zero)


def test_divide_negative():
    assert divide(-10, 2) == -5


def test_power_positive():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1


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
    (10, 5, 5),
    (3, 7, -4),
    (0, 0, 0),
    (-2, -3, 1),
])
def test_subtract_parametrized(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 7, 21),
    (0, 100, 0),
    (-2, 3, -6),
    (2.5, 4, 10.0),
])
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (7, 2, 3.5),
    (-10, 2, -5),
])
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -2, 0.25),
    (9, 0.5, 3.0),
])
def test_power_parametrized(a, b, expected):
    assert power(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [
    (5, 0),
    (-3, 0),
    (0, 0),
])
def test_divide_by_zero_parametrized(a, b):
    with pytest.raises(ValueError):
        divide(a, b)



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])   