import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import requests
from pages.page_papa_pizza.page_main import LoginPage

@allure.id("008")
@allure.label("Papa pizza")
@allure.title("Papa pizza проверка навигационного меню")
@allure.description("Тест проверяет что пользователь может перемещаться корректно по навигационное меню")
@pytest.mark.papa_pizza

def tests_007(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт Papa pizza"):
        login.open()

    with allure.step('Кликнуть "Да" в модальном окне'):
        login.click_modal_window()

    with allure.step('Кликнуть в навигационном меню на кнопку "Пицца"'):
        login.click_pizza_button_navbar()

    with allure.step('Проверяем что мы во вкладке "Пицца"'):
        assert login.wait_pizza_header(), "ОШИБКА не перешел по вкладке пицца"

    with allure.step('Кликнуть в навигационном меню на кнопку "Напитки"'):
        login.click_drinks_button_navbar()

    with allure.step('Проверяем что мы во вкладке "Напитки"'):
        assert login.wait_drinks_header(), "ОШИБКА не перешел по вкладке напитки"





