"""
1) Тесты с позитивными кейсами авторизации (корректный логин пользователя)
2) Негативные тесты (пользователь не найден или неверный логин)

Нужно использовать фикстуру будет возвращаться данные для авторизации
постараться использовать параметризацию
"""

import pytest
from auth_test.auth_simple.auth import login

@pytest.mark.authorization
@pytest.mark.parametrize("username, password", [
    ("admin", "admin123"),
    ("guest", "guest"),
    ("123", "123"),
    ("guest", "b"),
    (" ", " ")
])
def test_login(username, password):
    assert  login(username, password)

@pytest.fixture()
def get_data():
    return {"username": "admin",
            "password": "admin123"}

    # correct = {
    #"username": "admin",
            # "password": "admin123"
    # }

@pytest.fixture(scope="session")
def setup_and_teardown():
    print("Подготовка соединения")
    resource = {
        "connect": True
    }
    yield resource
    print("Разрыв соединения")
    resource["connect"] = False

