from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_create_new_board(self):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Create new board']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("arguments[0].click();", button)

    def enter_board_title(self, title):
        input_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Add board title']")))
        input_field.send_keys(title)
        assert input_field.get_attribute("value") == title

    def click_create_board(self):
        create_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="new-board-create"]')))
        self.driver.execute_script("arguments[0].click();", create_button)
