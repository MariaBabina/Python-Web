from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Task4.pages.base_page import BasePage

class ContactPage(BasePage):
    # Локаторы формы
    contact_name_field = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='text']")
    contact_email_field = (By.CSS_SELECTOR, "input.mdc-text-field__input[type='email']")
    contact_message_field = (By.CSS_SELECTOR, "textarea.mdc-text-field__input")
    submit_button = (By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised")

    def go_to_contact_us(self):
        """Переход на страницу Contact Us"""
        self.find_element((By.LINK_TEXT, "Contact")).click()

    def enter_contact_name(self, name):
        """Ввод имени"""
        self.enter_text(self.contact_name_field, name)

    def enter_contact_email(self, email):
        """Ввод email"""
        self.enter_text(self.contact_email_field, email)

    def enter_contact_message(self, message):
        """Ввод сообщения"""
        self.enter_text(self.contact_message_field, message)

    def submit_contact_form(self):
        """Отправляем форму"""
        self.find_element(self.submit_button).click()

    def is_submission_successful(self):
        """Проверка успешной отправки через alert или сообщение на странице"""
        try:
            # Явное ожидание появления alert
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"DEBUG: Alert text is '{alert_text}'")
            alert.accept()
            return alert_text == "Form successfully submitted"
        except Exception as e:
            print(f"DEBUG: No alert found or error occurred: {e}")
            # Если alert отсутствует, ищем текст подтверждения на странице
            try:
                success_message = self.find_element((By.CSS_SELECTOR, ".success-message"))  # Локатор сообщения
                if success_message:
                    print(f"DEBUG: Success message found: {success_message.text}")
                    return "Form successfully submitted" in success_message.text
            except Exception as ex:
                print(f"DEBUG: No success message found: {ex}")
            return False
