import requests
import yaml
import pytest

# Загружаем данные из config.yaml
with open("config.yaml") as f:
    data = yaml.safe_load(f)
address = data["address"]

@pytest.fixture
def login():
    # Заголовок для авторизации
    login_data = {"username": data["username"], "password": data["password"]}
    response = requests.post(f"{address}/gateway/login", data=login_data)
    return response.json().get("token")

@pytest.mark.parametrize("title, description, content", [
    ("Новый пост", "Описание нового поста", "Содержимое нового поста")
])
def test_create_and_check_post(login, title, description, content):
    # Заголовок с токеном авторизации
    headers = {"X-Auth-Token": login}

    # Создаем новый пост
    create_res = requests.post(
        f"{address}/api/posts",
        headers=headers,
        data={"title": title, "description": description, "content": content}
    )
    
    # Диагностика: выводим ответ сервера при создании поста
    print("Ответ при создании поста:", create_res.json())
    
    # Проверяем, что пост создан успешно с ожидаемым статусом
    assert create_res.status_code in [200, 201], "Не удалось создать пост"
    
    # Проверяем, что пост теперь доступен на сервере
    res = requests.get(
        f"{address}/api/posts",
        headers=headers
    )
    listres = [i["description"] for i in res.json().get("data", [])]
    assert description in listres, "Пост не найден на сервере"
