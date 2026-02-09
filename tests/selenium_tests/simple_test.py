from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("")
chrome.close() # закрывает одну страницу
chrome.quit()
try:
    text = ""
    element = chrome.find_elements(by="xpath", value=f"//span[text()='{text}']")
except NoSuchElementException as e:
    print(f"На ноль делить нельзяю Оштбка: {e}")
else:
    print("Деление прошло успешно, все хорошо")
finally:
    print("Тут мы пытались выполнить деления")

"""
Autotest Code
|
WebDriver API
|
WebDriver (browser api)
|
Браузер
"""