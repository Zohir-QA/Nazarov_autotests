import allure
import pytest
import requests

@allure.id("1")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Получение biospecimens от nasa_api")
@allure.description("Тест проверяет что в ручке экспериментов приходят эксперименты")

def test_get_biospecimens():
    response = requests.get(url)
    my_json = response.json()
    subjects = my_json.get('data')
    val = 'https://osdr.nasa.gov/geode-py/ws/api/biospecimen/24913'
    for item in subjects:
        biospecimen_id = item.get('id')
        identifier = item.get('identifier')  # например, "24913"
        print(f"ID: {biospecimen_id}, Identifier: {identifier}")
    # for i in subjects:
    #     if i.get("biospecimen") == val:
    #         subj_response = requests.get(val)
    #         print(subj_response.json())
    #         print(subj_response.status_code)
    #         assert subj_response.status_code != 500
    print(response.status_code)
    assert response.status_code == 200



