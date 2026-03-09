import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import requests

@allure.id("002")
@allure.label("Yandex")
@allure.title("Yandex проверка карточки товара")
@allure.description("Тест проверяет весь путь до карточка товара и открытие самой карточки товара")

def tests_002(driver):
    with allure.step("Открываем сайт яндекс маркет"):
        driver.get("https://market.yandex.ru/")

    with allure.step("Кликаем в шапке 'Электроника'"):
        header = driver.find_element(By.XPATH, '//span [text()="Электроника"]')
        header.click()

    with allure.step("Кликаем 'Смартфоны и гаджеты'"):
        smartphones = driver.find_element(By.XPATH, '//span[text()="Смартфоны и гаджеты"]')
        smartphones.click()

    time.sleep(1)
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    with allure.step("Кликаем на первый товар"):
        first_product_link = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="_1ENFO"]'))
        )
        first_product_link.click()

    time.sleep(1)
    handles_1 = driver.window_handles
    driver.switch_to.window(handles_1[2])

    with allure.step("Товар успешно открыт"):
        title_element = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//h1[@data-additional-zone="title"]'))
        )

    product_name = title_element.text
    print(f"Название товара: {product_name}")

