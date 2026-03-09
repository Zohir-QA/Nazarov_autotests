"""
1) Тесты с позитивными кейсами авторизации (корректный логин пользователя)
2) Негативные тесты (пользователь не найден или неверный логин)

Нужно использовать фикстуру будет возвращаться данные для авторизации
постараться использовать параметризацию
"""

import pytest
from auth_test.auth_simple.auth import login

# @pytest.mark.authorization
# @pytest.mark.parametrize("username, password", [
#     ("admin", "admin123"),
#     ("guest", "guest"),
#     ("123", "123"),
#     ("guest", "b"),
#     (" ", " ")
# ])
# def test_login(username, password):
#     assert  login(username, password)

@pytest.fixture()
def get_data():
    return {"positive_1": {"username": "admin", "password": "admin123",},
            "positive_2": {"username": "guest", "password": "guest",},
            "negative_1": {"username": "123", "password": "123",},
            "negative_2": {"username": "guest", "password": "b",},
            "negative_3": {"username": " ", "password": " ",}
}

@pytest.mark.authorization
def test_positive_login(get_data):
    user = get_data.get("positive_1")
    assert login(user.get("username"), user.get("password"))

@pytest.mark.authorization
def test_positive_login(get_data):
    user = get_data.get("positive_2")
    assert login(user.get("username"), user.get("password"))

@pytest.mark.authorization
def test_negative_login(get_data):
    user = get_data.get("negative_1")
    assert login(user.get("username"), user.get("password"))

@pytest.mark.authorization
def test_negative_login(get_data):
    user = get_data.get("negative_2")
    assert login(user.get("username"), user.get("password"))

@pytest.mark.authorization
def test_negative_login(get_data):
    user = get_data.get("negative_3")
    assert login(user.get("username"), user.get("password"))







# попытка в сортировку
# @pytest.fixture()
# def get_data():
#     return {"positive":[{"login": "admin", "password": "admin123",},
#                         {"login": "guest", "password": "guest",}],
#             "negative":[{"login": "123", "password": "123",},
#                         {"login": "guest", "password": "b",},
#                         {"login": " ", "password": " ",}]
# }

# @pytest.mark.authorization
# def test_positive_login(get_data):
#     for user_data in get_data["positive"]:
#         assert login(user_data["login"], user_data["password"])
#
# @pytest.mark.authorization
# def test_negative_login(get_data):
#     for user_data in get_data["negative"]:
#         assert login(user_data["login"], user_data["password"])
