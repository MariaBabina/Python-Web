import requests
from Task4.config.config import testdata  # Исправленный импорт
from Task4.utils.logger import logger  # Исправленный импорт

class APIClient:
    def __init__(self):
        self.base_url = testdata["address"]

    def login(self, username, password):
        url = f"{self.base_url}/gateway/login"
        try:
            response = requests.post(url, data={"username": username, "password": password})
            response.raise_for_status()
            logger.info("Successfully logged in.")
            return response.json().get("token")
        except requests.exceptions.RequestException as e:
            logger.error(f"Login failed: {e}")
            return None

    def create_post(self, title, description, content, token):
        url = f"{self.base_url}/api/posts"
        headers = {"X-Auth-Token": token}
        try:
            response = requests.post(
                url,
                headers=headers,
                data={"title": title, "description": description, "content": content}
            )
            response.raise_for_status()
            logger.info("Post created successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to create post: {e}")
            return None
