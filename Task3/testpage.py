from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time

class TestPageLocators:
    LOCATOR_LOGIN_USERNAME = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='text']")
    LOCATOR_LOGIN_PASSWORD = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='password']")
    LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOCATOR_CONTACT_LINK = (By.CSS_SELECTOR, "a[href='/contact']")
    LOCATOR_CONTACT_NAME = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='text']")
    LOCATOR_CONTACT_EMAIL = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='email']")
    LOCATOR_CONTACT_CONTENT = (By.CSS_SELECTOR, "textarea.mdc-text-field__input")
    LOCATOR_CONTACT_SUBMIT = (By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised")

class OperationsHelper(BasePage):
    def enter_username(self, username):
        username_field = self.find_element(TestPageLocators.LOCATOR_LOGIN_USERNAME)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find_element(TestPageLocators.LOCATOR_LOGIN_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element(TestPageLocators.LOCATOR_LOGIN_BUTTON)
        login_button.click()

    def go_to_contact_us(self):
        time.sleep(3)  # Дополнительное ожидание для загрузки страницы
        contact_link = self.find_element(TestPageLocators.LOCATOR_CONTACT_LINK)
        contact_link.click()

    def enter_contact_name(self, name):
        name_field = self.find_element(TestPageLocators.LOCATOR_CONTACT_NAME)
        name_field.clear()
        name_field.send_keys(name)

    def enter_contact_email(self, email):
        email_field = self.find_element(TestPageLocators.LOCATOR_CONTACT_EMAIL)
        email_field.clear()
        email_field.send_keys(email)

    def enter_contact_content(self, content):
        content_field = self.find_element(TestPageLocators.LOCATOR_CONTACT_CONTENT)
        content_field.clear()
        content_field.send_keys(content)

    def click_submit_button(self):
        submit_button = self.find_element(TestPageLocators.LOCATOR_CONTACT_SUBMIT)
        submit_button.click()
