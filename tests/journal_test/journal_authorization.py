from selenium.webdriver.common.by import By
def test_authorization(driver):
    driver.get("https://journal.top-academy.ru/ru/auth/login/index")
    username = driver.find_element(By.XPATH, '//input[@id="username"]')
    username.click()
    username.send_keys("Nazar_nf14")

    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.click()
    password.send_keys("QJ7R449b")

    password = driver.find_element(By.XPATH, '//button[@type="submit"]')
    password.click()