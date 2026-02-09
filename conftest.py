import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(10)

    yield chrome # закрывает, после него не чего не писать
    chrome.quit()