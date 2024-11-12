import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Загружаем данные из testdata.yaml
with open("Task3/testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture(scope="session")
def browser():
    # Настраиваем браузер на основе testdata.yaml
    browser = testdata.get("browser", "chrome").lower()
    if browser == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = ChromeService(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
