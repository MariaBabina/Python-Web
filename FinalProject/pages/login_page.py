from selenium.webdriver.common.by import By
from FinalProject.pages.base_page import BasePage
from FinalProject.utils.logger import logger
from FinalProject.config.config import testdata

class LoginPage(BasePage):
    # Локаторы формы
    username_field = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='text']")
    password_field = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='password']")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    blog_widget = (By.XPATH, "//h1[text()='Blog']")

    def do_login_and_wait(self):
        logger.info("Starting login ...")  # Логирование начала
        self.go_to_site()

        # Логирование перед входом
        logger.info("Attempting login with username and password")
        self.__login(testdata["username"], testdata["password"])

        # Ждем успешного входа
        assert self.__wait_login(), "Login is failed !"

        # Логируем успешный вход
        logger.info(f"Current URL after login: {self.driver.current_url}")

    def __login(self, username, password):
        """Метод для авторизации"""
        # Проверяем доступность формы перед вводом
        assert self.is_element_visible(self.username_field), "Username field not visible"
        assert self.is_element_visible(self.password_field), "Password field not visible"
        assert self.is_element_visible(self.login_button), "Login button not visible"

        # Вводим данные и кликаем по кнопке
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.find_element(self.login_button).click()

    def __wait_login(self, timeout = 5):
        return self.is_element_visible(self.blog_widget, timeout)
