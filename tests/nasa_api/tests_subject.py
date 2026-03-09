import allure
import pytest
import requests

@allure.id("005")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Получение subject от nasa_api")
@allure.description("Тест проверяет, что эндпоинт экспериментов возвращает список предметов")

def tests_005():
    with allure.step("Тест получения списка предметов из NASA OSDR API"):
        url = 'https://osdr.nasa.gov/geode-py/ws/api/subjects'
    with allure.step("Выполняем GET-запрос"):
        response = requests.get(url)
    with allure.step("Парсим JSON-ответ"):
        my_json = response.json()
        subjects = my_json.get('data')
    with allure.step("Логируем найденные предметов"):
        for subj in subjects:
            val = "https://osdr.nasa.gov/geode-py/ws/api/subjects/195"
            if subj.get("subject") == val:
                subj_response = requests.get(val)
                print(subj_response.json())
                print(subj_response.status_code)
                assert subj_response.status_code != 500
    with allure.step("Успешно получения списка предметов"):
        print(response.status_code)
        assert response.status_code == 200