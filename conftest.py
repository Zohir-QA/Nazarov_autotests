import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import requests

# @pytest.fixture(scope='module')
# def setup_and_teardown(request):
#     print('Подготовка')
#     resource = {"connected": True}
#
#     def clear_connection():
#         print("Очистка")
#         resource["connected"] = False
#
#     request.addfinalize(clear_connection())
#
#

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(10)

    yield chrome # закрывает, после него не чего не писать
    chrome.quit()