import pytest

@pytest.mark.multiplication # - Тесты для операции умножения
@pytest.mark.parametrize("a, b, expected_value", [
    (2, 3, 6),
    (0, 10, 0),
    (2, 2, 0),
    (-5, -5, 25),
    (2, 1, 1)
])
def test_multiplication_positive(a, b, expected_value):
    assert a * b == expected_value, f"{a}*{b} получилось {expected_value}"

@pytest.mark.division
@pytest.mark.parametrize("a, b, expected_value", [
    (6, 3, 2),
    (10, 2, 5),
    (-1, -2, 5),
    (0, 5, 0),
    (100, 25, 4),
    (5, 5, 0)
])
def test_division_positive(a, b, expected_value):
    assert a / b == expected_value, f"{a}/{b} получилось {expected_value}"