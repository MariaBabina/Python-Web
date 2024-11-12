from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"  # Тестируемая URL

    def find_element(self, locator, time=10):
        """Метод для поиска элемента с ожиданием его появления"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )

    def go_to_site(self):
        """Переход на главную страницу"""
        self.driver.get(self.base_url)
