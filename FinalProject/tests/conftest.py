import pytest
import sys
import os

# Добавляем путь проекта в sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_path)

# Для отладки выводим текущие пути
# print("DEBUG: PYTHONPATH =", sys.path)

@pytest.fixture(scope="function")
def browser():
    """Инициализация веб-драйвера для тестов"""
    from selenium import webdriver  # Импортируем здесь, чтобы избежать лишних ошибок
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)  # Ожидание 3 секунды
    driver.maximize_window()
    yield driver
    driver.quit()
