import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import requests
from pages.page_papa_pizza.page_main import LoginPage

@allure.id("006")
@allure.label("Papa pizza")
@allure.title("Papa pizza проверка шапки")
@allure.description("Тест проверяет что все кнопки нажимаются и перекидывают во вкладки в шапке")
@pytest.mark.papa_pizza

def tests_006(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт Papa pizza"):
        login.open()

    with allure.step('Кликнуть "Да" в модальном окне'):
        login.click_modal_window()

    with allure.step('Кликнуть на кнопку "Акции"'):
        login.click_stock()

    with allure.step('Проверяем что вкладке "Акции" успешно открыта'):
        assert login.wait_our_promotions(), "ОШИБКА не перешел по вкладке акции"

    with allure.step('Кликнуть на кнопку "Условия доставки"'):
        login.click_delivery_terms()

    with allure.step('Проверяем что вкладке "Условия доставки" успешно открыта'):
        assert login.wait_delivery(), "ОШИБКА не перешел по вкладке условия доставки"

    with allure.step('Кликнуть на кнопку "Оплата"'):
        login.click_payment()

    with allure.step('Проверяем что вкладке "Оплата" успешно открыта'):
        assert login.wait_payment_header(), "ОШИБКА не перешел по вкладке оплата"
