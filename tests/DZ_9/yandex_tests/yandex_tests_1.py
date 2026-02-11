import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
def test_yandex(driver):
    driver.get("https://market.yandex.ru/")
    header = driver.find_element(By.XPATH, '//span [text()="Электроника"]')
    header.click()

    smartphones = driver.find_element(By.XPATH, '//span[text()="Смартфоны и гаджеты"]')
    smartphones.click()

    time.sleep(1)
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    first_product_link = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="_1ENFO"]'))
    )
    first_product_link.click()

    time.sleep(1)
    handles_1 = driver.window_handles
    driver.switch_to.window(handles_1[2])

    title_element = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//h1[@data-additional-zone="title"]'))
    )

    product_name = title_element.text
    print(f"Название товара: {product_name}")

