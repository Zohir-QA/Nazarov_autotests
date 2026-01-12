import pytest

@pytest.fixture()
def get_data():
    return {"a": 2,
            "b": 5}

@pytest.fixture(scope="session")
def setup_and_teardown():
    print("Подготовка соединения")
    resource = {
        "connect": True
    }
    yield resource
    print("Разрыв соединения")
    resource["connect"] = False

    """
    SCOPE – позволяет управлять тем, когда текстура должна управляться 
    
    scope=function – фикстура выполнится 1 раз каждой функции с тестом
    scope=modul – фикстура выполнится 1 раз для всего модуля с тестами
    scope=session - фикстура выполнится 1 раз для всей сессии с запуском тестов
    """