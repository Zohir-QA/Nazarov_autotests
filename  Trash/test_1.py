import pytest
import allure
from conftest import driver
from selenium import webdriver

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

# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")

# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     return driver

@pytest.fixture(scope="function")

def get_screenshot(driver):
    yield
    if hasattr(driver, "get_screenshot_as_png"):
        allure.attach(
            driver.get_screenshot_as_png(),
            name="my_screenshot",
            attachment_type=allure.attachment_type.PNG
    )

@pytest.mark.connection
def test_connection(setup_and_teardown):
    with allure.step("Выполняю первый шаг моего теста"):
        assert setup_and_teardown["connect"] == True
    with allure.step("Выполняю второй шаг моего теста"):
        # screenshot = driver.get_screenshot_as_png()
        # allure.attach(screenshot, name='my_screenshot')
        text = "Какой-то текст"
        allure.attach(body=text, name="my_text", attachment_type=allure.attachment_type.TEXT)

@pytest.mark.connecrion
def test_connection_1(setup_and_teardown):
    assert setup_and_teardown["connect"] == True
