from web_site import Site
import time
from selenium.common.exceptions import TimeoutException

def test_step1(x_selector1, x_selector2, btn_selector, x_selector4, er2, post_input_selector, post_description_selector, post_submit_selector, post_title):
    # Создаем экземпляр Site, который автоматически загрузит URL и данные авторизации из testdata.yaml
    site = Site()

    # Входим в систему
    site.login()

    # Проверка на наличие приветственного текста
    try:
        user_label = site.find_element("xpath", x_selector4)
        text = user_label.text
        assert text == er2
        print("Успешный вход в систему.")
    except TimeoutException:
        print("Ошибка: Не удалось найти элемент приветствия после входа.")
        site.quit()
        return

    # Ждем полной загрузки страницы
    time.sleep(5)

    # Попытка нажать на кнопку создания поста
    try:
        create_post_btn = site.find_element("css selector", post_submit_selector)
        create_post_btn.click()
        print("Кнопка создания поста успешно нажата.")
    except TimeoutException:
        print("Ошибка: Не удалось найти кнопку создания поста.")
        site.quit()
        return

    # Ждем, чтобы форма загрузилась
    time.sleep(5)

    # Попытка ввести заголовок поста
    try:
        title_input = site.find_element("css selector", post_input_selector)
        title_input.send_keys(post_title)
        print("Заголовок поста успешно введен.")
    except TimeoutException:
        print("Ошибка: Не удалось найти поле для ввода заголовка поста.")
        site.quit()
        return

    # Попытка ввести описание поста
    try:
        description_input = site.find_element("css selector", post_description_selector)
        description_input.send_keys("This is a test post description.")
        print("Описание поста успешно введено.")
    except TimeoutException:
        print("Ошибка: Не удалось найти поле для ввода описания поста.")
        site.quit()
        return

    # Попытка нажать на кнопку сохранения поста
    try:
        save_btn = site.find_element("css selector", post_submit_selector)
        save_btn.click()
        print("Кнопка сохранения поста успешно нажата.")
    except TimeoutException:
        print("Ошибка: Не удалось найти кнопку сохранения поста.")
        site.quit()
        return

    # Ждем завершения создания поста
    time.sleep(5)

    # Завершаем работу с драйвером
    site.quit()
