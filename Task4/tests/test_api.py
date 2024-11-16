import requests
import pytest
from Task4.utils.api_client import APIClient
from Task4.config.config import testdata  # Убедились, что путь корректный
from Task4.utils.logger import logger


@pytest.fixture
def api_client():
    return APIClient()


def test_login(api_client):
    """Тест на проверку авторизации через API."""
    logger.info("Starting API login test")
    token = api_client.login(testdata["username"], testdata["password"])
    assert token, "Login failed, token not received"


@pytest.mark.parametrize("title, description, content", [
    ("Test Title", "Test Description", "Test Content"),
    ("Second Post", "Second Description", "Second Content")
])
def test_create_post(api_client, title, description, content):
    """Тест на создание поста через API."""
    logger.info(f"Starting API test for creating post: {title}")
    token = api_client.login(testdata["username"], testdata["password"])
    assert token, "Login failed, token not received"

    response = api_client.create_post(title, description, content, token)
    assert response, "Post creation failed"

    # Проверяем, что пост создан и есть на сервере
    created_description = response.get("description")
    assert created_description == description, "Description mismatch in the created post"
    logger.info(f"Post created successfully: {title}")
