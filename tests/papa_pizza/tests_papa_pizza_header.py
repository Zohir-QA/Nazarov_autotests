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
@allure.description("Тест проверяет весь путь до карточка товара и открытие самой карточки товара")

def tests_006(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт Papa pizza"):
        login.open()

    with allure.step('Кликнуть "Да" в модальном окне'):
        login.click_modal_window()

    with allure.step('Кликнуть на кнопку "Акции"'):
        login.click_aktsii()

    with allure.step('Кликнуть на кнопку "Условия доставки"'):
        login.click_usloviya_dostavki()
