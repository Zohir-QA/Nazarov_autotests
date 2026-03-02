import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(10)

    yield chrome # закрывает, после него не чего не писать
    chrome.quit()