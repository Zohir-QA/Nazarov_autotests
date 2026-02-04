from selenium import webdriver


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("")
chrome.close() # закрывает одну страницу
chrome.quit()

"""
Autotest Code
|
WebDriver API
|
WebDriver (browser api)
|
Браузер
"""