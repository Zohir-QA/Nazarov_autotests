from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL = "http://papapizza59.ru/"
    MODAL_WINDOW = (By.XPATH, '//a[@class="popup-modal-dismiss"]')
    USLOVIYA_DOSTAVKI = (By.XPATH, '//a[@href="http://papapizza59.ru/dostavka"]')
    AKTSII = (By.XPATH, '//a[@href="http://papapizza59.ru/nashi_akcii"]')
    FIRST_PRODUCT_LINK = (By.XPATH, '//div[@class="_1ENFO"]')
    TITLE_ELEMENT = (By.XPATH, '//h1[@data-additional-zone="title"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_modal_window(self):
        self.click(self.MODAL_WINDOW)

    def open(self):
        self.driver.get(self.URL)
        return self

    def click_aktsii(self):
        self.click(self.AKTSII)

    def click_usloviya_dostavki(self):
        self.click(self.USLOVIYA_DOSTAVKI)

    def click_first_product_link(self):
        self.click(self.SMARTPHONES)

    def get_text(self, locator):
        return self.driver.find_element(locator).text