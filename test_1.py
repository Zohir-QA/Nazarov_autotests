import pytest

@pytest.mark.regress # - тесты для регрессионых проверок
@pytest.mark.parametrize("a, b, expected_value",[
    (2,2,4),
    (2,2,0),
    (5,5,10),
    (5,5,5)
])
def test_simple(a, b, expected_value):
    assert  a+b == expected_value, f"{a}+{b} получилось {expected_value}"

@pytest.mark.smoke
def test_string():
    assert "Hello" in "Hello word"

def test_summ_numbers(get_data):
    data = get_data
    assert data["a"] + data["b"] == 7

@pytest.mark.connection
def test_connection(setup_and_teardown):
    assert setup_and_teardown["connect"] == True

@pytest.mark.connecrion
def test_connection_1(setup_and_teardown):
    assert setup_and_teardown["connect"] == True
