import pytest
from Task4.pages.login_page import LoginPage
from Task4.config.config import testdata
from Task4.utils.logger import logger
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
def test_login(browser):
    logger.info("Starting login test")  # Логирование начала теста
    page = LoginPage(browser)
    page.go_to_site()

    # Логирование перед входом
    logger.info("Attempting login with username and password")
    page.login(testdata["username"], testdata["password"])
    
    # Ждем, пока прогрузится главная страница после успешного логина
    assert page.wait_login(), "Login is failed !"
  
    # Логирование успешного входа
    current_url = browser.current_url.rstrip('/')  # Убираем слэш с конца
    expected_url = testdata["address"]   # Ожидаемый адрес из testdata
    logger.info(f"Current URL: {current_url}")  # Логируем текущий URL
    assert current_url == expected_url, f"Login failed: expected {expected_url}, but got {current_url}"
    logger.info("Login successful, redirected to the home page.")
