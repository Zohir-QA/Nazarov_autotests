from unittest import expectedFailure

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()


# Поиск элементов на странице

driver.find_element(By.XPATH, "//div[text() = 'Hello']") # поиск элемента на экране

# работа с элементами
element = driver.find_element()

element.click() # нажатие элемента

element.send_keys("Текст который я ввожу") # ввод текста в элемент

element.clear() # очистка текстового поля

element.submit() # подтверждение и отправка форм

# работа с окнами и вкладками

windows = driver.window_handles # получение всех окон браузера

driver.switch_to.window(windows[0]) # переключение всех окон браузера

driver.switch_to.frame(windows[0]) # переключение на другой фрейм

driver.switch_to.default_content() # возвращение в основной контекст страницы

# Ожидания (Implicit waits, explicit waits)

driver.implicitly_wait(10) # задаем неявное ожидание

WebDriverWait(driver,10).until(
    expected_conditions.invisibility_of_element_located((By.XPATH, "//div"))
) # задаем явное ожидание элемента

# получение информации о странице

title = driver.title # получаем тайт страницы

current_url = driver.current_url # получение текущего урла страницы

page_source = driver.page_source # получение текущего кода страницы

element_attrs = element.get_attribute("text") # получение значения аттрибута у элемента

text = element.text # получение текста у элемента


# работа с алертами/pop-up

alert = driver.switch_to.alert # переключение контекста на алерт

alert.accept() # принятие алерта
alert.dismiss() # отклонение алерта
alert.send_keys("text") #  ввод текста в алерт
alert_text = alert.text # получение текста из алерта

# скриншоты

driver.get_screenshot_as_file("test/my_screenshot.png") # сохранения скриншота в определенный файл

# работа с прокруткой страницы

driver.execute_script()
