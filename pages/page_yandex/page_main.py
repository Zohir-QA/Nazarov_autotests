from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL = "https://market.yandex.ru/"
    EMAIL_INPUT = (By.ID, "email")
    SMARTPHONES = (By.XPATH, '//span[text()="Смартфоны и гаджеты"]')
    ELEKTRONIKA = (By.XPATH, '//span [text()="Электроника"]')
    FIRST_PRODUCT_LINK = (By.XPATH, '//div[@class="_1ENFO"]')
    TITLE_ELEMENT = (By.XPATH, '//h1[@data-additional-zone="title"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def click_elektronika(self):
        self.click(self.ELEKTRONIKA)

    def click_smartphones(self):
        self.click(self.SMARTPHONES)

    def click_first_product_link(self):
        self.click(self.SMARTPHONES)

    def get_text(self, locator):
        return self.driver.find_element(locator).text