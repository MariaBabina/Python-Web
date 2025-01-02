import os
import sys
import time

# Явно добавляем путь до `FinalProject` в `sys.path`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
from FinalProject.pages.login_page import LoginPage
from FinalProject.pages.about_page import AboutPage
from FinalProject.utils.logger import logger
from FinalProject.config.config import testdata

@pytest.mark.usefixtures("browser")
def test_about_loaded(browser):
    # логин
    login_page = LoginPage(browser)
    login_page.do_login_and_wait()

    # Переход на страницу "Contact Us"
    about_page = AboutPage(browser)
    about_page.go_to_page_and_wait()


@pytest.mark.usefixtures("browser")
def test_header_font_size_is_32px(browser):
    # логин
    login_page = LoginPage(browser)
    login_page.do_login_and_wait()

    # Переход на страницу "Contact Us"
    about_page = AboutPage(browser)
    about_page.go_to_page_and_wait()

    element = browser.find_element(*about_page.header_element)
    font_size = element.value_of_css_property("font-size")
    assert font_size == "32px", "Header's font size is not 32px!"
