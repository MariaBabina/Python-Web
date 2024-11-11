import pytest
import yaml
import requests

# Загружаем данные из config.yaml
with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    # Выполняем запрос для авторизации
    res = requests.post(
        data["address"] + "/gateway/login",
        data={"username": data["username"], "password": data["password"]}
    )
    # Проверяем содержимое ответа
    print(res.content)
    # Возвращаем токен из ответа
    return res.json().get("token")
