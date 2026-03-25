from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators

class LoginPage(BasePage):
    # URL = "http://papapizza59.ru/"
    # MODAL_WINDOW = (By.XPATH, '//a[@class="popup-modal-dismiss"]')
    # USLOVIYA_DOSTAVKI = (By.XPATH, '//a[text() = "Условия доставки"and not(@rel="nofollow")]')
    # AKTSII = (By.XPATH, '//a[@href="http://papapizza59.ru/nashi_akcii" and not(@rel="nofollow")]')
    # OPLATA = (By.XPATH, '//div[contains(@class, "top-links")]//a[@href="http://papapizza59.ru/oplata"]')
    # NASHI_AKTSII = (By.XPATH, '//h1[text() = "Наши акции"]')
    # DOSTAVKA = (By.XPATH, '//h1[text() = "Доставка"]')
    # ZAGOLOVOK_OPLATY = (By.XPATH, '//h1[text() = "Оплата"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = MainPageLocators

    def click_modal_window(self):
        self.click(self.locators.MODAL_WINDOW)

    def open(self):
        self.driver.get(self.locators.URL)
        return self

    def click_stock(self):
        self.click(self.locators.STOCK)

    def click_delivery_terms(self):
        self.click(self.locators.DELIVERY_TERMS)

    def click_payment(self):
        self.click(self.locators.PAYMENT)

    def wait_our_promotions(self):
        return self.wait_element(self.locators.OUR_PROMOTIONS)

    def wait_delivery(self):
        return self.wait_element(self.locators.DELIVERY)

    def wait_payment_header(self):
        return self.wait_element(self.locators.PAYMENT_HEADER)

    def click_pizza_button_navbar(self):
        self.click(self.locators.PIZZA_BUTTON_NAVBAR)

    def wait_pizza_header(self):
        return self.wait_element(self.locators.PIZZA_HEADER)

    def click_main_image(self):
        self.click(self.locators.MAIN_IMAGE)

    def wait_main_title(self):
        return self.wait_element(self.locators.MAIN_TITLE)

    def click_drinks_button_navbar(self):
        self.click(self.locators.DRINKS_BUTTON_NAVBAR)

    def wait_drinks_header(self):
        return self.wait_element(self.locators.DRINKS_HEADER)

