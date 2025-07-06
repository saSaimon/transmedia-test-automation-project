from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:3000")

wait = WebDriverWait(driver, 10)

# Safe function to wait for new board without triggering stale element errors
def wait_for_board_to_appear(title, timeout=10):
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            boards = driver.find_elements(By.CSS_SELECTOR, '[data-cy="board-item"]')
            for b in boards:
                if title in b.text:
                    return b
        except:
            pass
        time.sleep(0.5)
    raise Exception(f"Board titled '{title}' not found after {timeout} seconds")

try:
    # Step 1: Click "Create new board"
    Board_Create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Create new board']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", Board_Create_button)
    time.sleep(0.3)
    driver.execute_script("arguments[0].click();", Board_Create_button)

    # Step 2: Input board title
    Board_input_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Add board title']")))
    Board_title = 'My Local Project'
    Board_input_field.send_keys(Board_title)

    # Step 3: Verify value
    actual_title = Board_input_field.get_attribute("value")
    assert Board_title == actual_title, f"Expected '{Board_title}', but got '{actual_title}'"

    # Step 4: Click "Create board"
    create_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="new-board-create"]')))
    driver.execute_script("arguments[0].click();", create_button)

    print("✅ Board created and opened successfully!")

    time.sleep(3)

    list_input_1 = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter list title...']")))
    list_input_1.send_keys("List 1")

    add_list_btn_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Add list")]')))
    add_list_btn_1.click()

    time.sleep(1)  # Give UI time to update

    # Step 5: Add second list
    list_input_2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-cy="add-list-input"]')))
    list_input_2.send_keys("List 2")

    add_list_btn_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Add list")]')))
    add_list_btn_2.click()

    time.sleep(1)

    # Step 6: Delete the first list (e.g., "List 1")

    # Wait for list to load
    first_list_options_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="list-options"]'))
    )

    # Open the dropdown
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_list_options_button)
    driver.execute_script("arguments[0].click();", first_list_options_button)

    # Wait for "Delete list" to appear and click
    delete_list_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="delete-list"]'))
    )
    driver.execute_script("arguments[0].click();", delete_list_button)

    print("🗑️ First list deleted successfully.")

finally:
    driver.quit()