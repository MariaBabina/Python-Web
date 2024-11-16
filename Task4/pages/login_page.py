from selenium.webdriver.common.by import By
from Task4.pages.base_page import BasePage  

class LoginPage(BasePage):
    # Локаторы формы
    username_field = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='text']")
    password_field = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='password']")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    blog_widget = (By.XPATH, "//h1[text()='Blog']")

    def login(self, username, password):
        """Метод для авторизации"""
        # Проверяем доступность формы перед вводом
        assert self.is_element_visible(self.username_field), "Username field not visible"
        assert self.is_element_visible(self.password_field), "Password field not visible"
        assert self.is_element_visible(self.login_button), "Login button not visible"

        # Вводим данные и кликаем по кнопке
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.find_element(self.login_button).click()

    def wait_login(self, timeout = 5):
        return self.is_element_visible(self.blog_widget, timeout)
        
