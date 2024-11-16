from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Task4.utils.logger import logger  # Исправленный импорт

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"  # Главная страница

    def go_to_site(self):
        try:
            self.driver.get(self.base_url)
            logger.info("Navigated to site")
        except Exception as e:
            logger.error(f"Failed to open site: {e}")

    def find_element(self, locator, time=2):  # Время ожидания 2 секунды
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator)
            )
            logger.info(f"Element found: {locator}")
            return element
        except Exception as e:
            logger.error(f"Could not find element {locator}: {e}")
            return None

    def enter_text(self, locator, text):
        """Метод для ввода текста в поле"""
        element = self.find_element(locator)
        if element:
            element.clear()  # Очищаем поле
            element.send_keys(text)  # Вводим текст
            logger.info(f"Entered text in {locator}: {text}")
        else:
            logger.error(f"Element {locator} not found for entering text.")

    def is_element_visible(self, locator, time=2):  # Время ожидания также уменьшено
        """Проверка видимости элемента на странице"""
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
