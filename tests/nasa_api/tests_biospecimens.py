import allure
import pytest
import requests

@allure.id("003")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Получение biospecimens от nasa_api")
@allure.description("Тест проверяет, что эндпоинт экспериментов возвращает данные биообразцов")

def tests_003():
    with allure.step("Тест получения списка биообразцов из NASA OSDR API"):
        url = 'https://osdr.nasa.gov/geode-py/ws/api/biospecimen/24913'
    with allure.step("Выполняем GET-запрос"):
        response = requests.get(url)
    with allure.step("Парсим JSON-ответ"):
        my_json = response.json()
    with allure.step("Логируем найденные биообразцы"):
        biospecimen_id = my_json.get('id')
        identifier = my_json.get('identifier')
        print(f"ID: {biospecimen_id}, Identifier: {identifier}")
    with allure.step("Успешно получения данные биообразца 24913"):
        print(response.status_code)
        assert response.status_code == 20024



