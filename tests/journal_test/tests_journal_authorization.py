from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import pytest
import requests

@allure.id("004")
@allure.label("Journal top-academy")
@allure.title("Journal проверка авторизации")
@allure.description("Тест проверяет авторизацию на положительный вариант и негативный")
def tests_authorization(driver):
    with allure.step("Открываем сайт journal"):
        driver.get("https://journal.top-academy.ru/ru/auth/login/index")

    with allure.step("Кликаем поле ввода логин и водим"):
        username = driver.find_element(By.XPATH, '//input[@id="username"]')
        username.click()
        username.send_keys("Nazar_nf14")

    with allure.step("Кликаем поле ввода пароль и водим"):
        password = driver.find_element(By.XPATH, '//input[@id="password"]')
        password.click()
        password.send_keys("QJ7R449b")

    with allure.step("Кликаем кнопку вход"):
        password = driver.find_element(By.XPATH, '//button[@type="submit"]')
        password.click()

    with allure.step("Пользователь успешно авторизован"):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH,
                                                               '//span [text()=" Посещаемость "]'))
        )