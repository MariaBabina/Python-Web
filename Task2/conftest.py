import pytest
import yaml

# Загружаем данные из testdata.yaml
with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def x_selector1():
    return "input.mdc-text-field__input"  # Поле для ввода имени пользователя

@pytest.fixture()
def x_selector2():
    return "input.mdc-text-field__input[type='password']"  # Поле для ввода пароля

@pytest.fixture()
def btn_selector():
    return "button.mdc-button.mdc-button--raised"  # Кнопка входа

@pytest.fixture()
def x_selector4():
    return "//*[@id='app']/main/nav/ul/li[3]/a"  # Селектор для приветственного текста

@pytest.fixture()
def er2():
    return "Hello, {}".format(testdata["username"])

@pytest.fixture()
def site_url():
    return testdata["address"]

@pytest.fixture()
def username():
    return testdata["username"]

@pytest.fixture()
def password():
    return testdata["password"]

@pytest.fixture()
def sleep_time():
    return testdata["sleep_time"]

# Селекторы для формы создания поста
@pytest.fixture()
def post_input_selector():
    return "input.mdc-text-field__input"  # Поле для заголовка поста

@pytest.fixture()
def post_description_selector():
    return "textarea.mdc-text-field__input"  # Поле для описания поста

@pytest.fixture()
def post_submit_selector():
    return "button.mdc-button.mdc-button--raised"  # Кнопка для сохранения поста

@pytest.fixture()
def post_title():
    return "My First Post"  # Заголовок поста
