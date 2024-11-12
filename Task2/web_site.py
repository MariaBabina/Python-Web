import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Site:
    def __init__(self):
        with open("testdata.yaml") as f:
            config = yaml.safe_load(f)
        
        self.url = config["address"]
        self.username = config["username"]
        self.password = config["password"]
        self.wait_time = config.get("sleep_time", 1)

        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
    
    def login(self):
        input1 = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='login']/div[1]/label/input"))
        )
        input2 = self.driver.find_element(By.XPATH, "//*[@id='login']/div[2]/label/input")
        btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        input1.send_keys(self.username)
        input2.send_keys(self.password)
        btn.click()
        
    def find_element(self, by, value):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((by, value))
        )

    def quit(self):
        self.driver.quit()
