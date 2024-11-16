import os
import sys

# Явно добавляем путь до `Task4` в `sys.path`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

print("DEBUG: sys.path =", sys.path)  # Выводим для проверки

import pytest
from Task4.pages.login_page import LoginPage
from Task4.pages.contact_page import ContactPage
from Task4.utils.logger import logger
from Task4.config.config import testdata

@pytest.mark.usefixtures("browser")
def test_contact_us(browser):
    logger.info("Starting login test")  # Логирование начала теста
    page = LoginPage(browser)  # Создаем объект LoginPage
    page.go_to_site()

    # Логирование перед входом
    logger.info("Attempting login with username and password")
    page.login(testdata["username"], testdata["password"])

    # Ждем успешного входа
    assert page.wait_login(), "Login is failed !"

    # Логируем успешный вход
    logger.info(f"Current URL after login: {browser.current_url}")

    # Переход на страницу "Contact Us"
    contact_page = ContactPage(browser)
    contact_page.go_to_contact_us()

    # Заполняем форму
    logger.info("Filling Contact Us form")
    contact_page.enter_contact_name(testdata["contact_name"])
    contact_page.enter_contact_email(testdata["contact_email"])
    contact_page.enter_contact_message(testdata["contact_message"])

    # Отправляем форму
    logger.info("Submitting the Contact Us form")
    contact_page.submit_contact_form()

    # Проверка, что форма была успешно отправлена
    is_successful = contact_page.is_submission_successful()
    logger.info(f"Form submission successful: {is_successful}")
    assert is_successful, "Contact Us form submission failed!"
