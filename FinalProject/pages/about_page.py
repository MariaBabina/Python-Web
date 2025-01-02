from selenium.webdriver.common.by import By
from FinalProject.pages.base_page import BasePage

class AboutPage(BasePage):
    # Локатор звголовка
    header_element = (By.CSS_SELECTOR, "h1.svelte-z9xc0")

    def go_to_page_and_wait(self):
        self.__go_to_page()
        # Ждем загрузки
        assert self.__wait_page_is_loaded(), "ABOUT page is not loaded!"

    def __go_to_page(self):
        """Переход на страницу"""
        self.find_element((By.LINK_TEXT, "About")).click()

    def __wait_page_is_loaded(self, timeout = 5):
        return self.is_element_visible(self.header_element, timeout)
