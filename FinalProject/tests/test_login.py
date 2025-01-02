import pytest
from FinalProject.pages.login_page import LoginPage
from FinalProject.config.config import testdata
from FinalProject.utils.logger import logger
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
def test_login(browser):
    logger.info("Starting login test")  # Логирование начала теста
    page = LoginPage(browser)
    page.do_login_and_wait()

    # Логирование успешного входа
    current_url = browser.current_url.rstrip('/')  # Убираем слэш с конца
    expected_url = testdata["address"]   # Ожидаемый адрес из testdata
    logger.info(f"Current URL: {current_url}")  # Логируем текущий URL
    assert current_url == expected_url, f"Login failed: expected {expected_url}, but got {current_url}"
    logger.info("Login successful, redirected to the home page.")
