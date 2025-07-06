from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BoardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_list(self, list_title):
        input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter list title...']")))
        input_box.send_keys(list_title)
        add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add list')]")))
        add_btn.click()
        time.sleep(1)

    def delete_first_list(self):
        options_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="list-options"]')))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", options_button)
        self.driver.execute_script("arguments[0].click();", options_button)
        delete_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="delete-list"]')))
        self.driver.execute_script("arguments[0].click();", delete_button)