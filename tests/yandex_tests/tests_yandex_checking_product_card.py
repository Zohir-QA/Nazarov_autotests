import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import requests
from pages.page_yandex.page_main import LoginPage

@allure.id("002")
@allure.label("Yandex")
@allure.title("Yandex проверка карточки товара")
@allure.description("Тест проверяет весь путь до карточка товара и открытие самой карточки товара")

def tests_002(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт яндекс маркет"):
        login.open()

    with allure.step("Кликаем в шапке 'Электроника'"):
        login.click_elektronika()

    with allure.step("Кликаем 'Смартфоны и гаджеты'"):
        login.click_smartphones()

    time.sleep(1)
    login.window(1)

    with allure.step("Кликаем на первый товар"):
        login.wait_element(login.FIRST_PRODUCT_LINK)
        login.click_first_product_link()

    time.sleep(1)
    handles_1 = driver.window_handles
    driver.switch_to.window(handles_1[2])

    with allure.step("Товар успешно открыт"):
        title_element = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//h1[@data-additional-zone="title"]'))
        )

    product_name = title_element.text
    print(f"Название товара: {product_name}")

