from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
def test_yandex(driver):
    driver.get("https://market.yandex.ru/")
    header = driver.find_element(By.XPATH, '//span[text()="Продавайте на Маркете"]')
    header.click()

    listbox = driver.find_element(By.XPATH, '//button[@class="Button2 Button2_size_m Select2-Button"]')
    listbox.click()

    img = driver.find_element(By.XPATH, '//img[@src="https://avatars.mds.yandex.net/get-lpc/12373972/e95b3019-49ed-4999-ba8d-8e0d94ab001b/orig?width=468&height=520"]')
    old_src = img.get_attribute("src")

    option = driver.find_element(By.XPATH, '//div[@data-key="item-2"]')
    option.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                                           '//img[@src="https://avatars.mds.yandex.net/get-lpc/12373972/12371d0a-48ab-447d-a4b3-4aa516ad333d/orig?width=500&height=520"]'))
    )

    new_img = driver.find_element(By.XPATH, '//img[@src="https://avatars.mds.yandex.net/get-lpc/12373972/12371d0a-48ab-447d-a4b3-4aa516ad333d/orig?width=500&height=520"]')
    new_src = new_img.get_attribute("src")

    assert old_src != new_src, f"Изображение не изменилось! Старый src: {old_src}, Новый src: {new_src}"