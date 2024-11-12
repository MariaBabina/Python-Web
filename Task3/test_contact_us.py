import pytest
from testpage import OperationsHelper  # Используем OperationsHelper для работы с формой
import yaml
import time

# Загружаем данные из testdata.yaml
with open("Task3/testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.mark.usefixtures("browser")
def test_contact_us_form(browser):
    page = OperationsHelper(browser)
    page.go_to_site()

    # Авторизация на сайте
    page.enter_username(testdata["username"])
    page.enter_password(testdata["password"])
    page.click_login_button()

    # Пауза для ожидания загрузки главной страницы после логина
    browser.implicitly_wait(5)

    # Переход на страницу Contact Us
    page.go_to_contact_us()

    # Ввод данных в форму Contact Us
    page.enter_contact_name(testdata["contact_name"])
    page.enter_contact_email(testdata["contact_email"])
    page.enter_contact_content(testdata["contact_message"])

    # Отправка формы и проверка alert
    page.click_submit_button()

    # Пауза перед проверкой alert, чтобы он успел появиться
    time.sleep(3)  # Пауза на 3 секунды перед проверкой alert
    alert = browser.switch_to.alert
    assert alert.text == testdata["expected_alert_text"]
    alert.accept()
