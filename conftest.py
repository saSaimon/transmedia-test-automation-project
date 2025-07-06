# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:3000")
    yield driver
    driver.quit()