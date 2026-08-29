"""
Test Suite: Dropdown & Dynamic Content
Target: https://the-internet.herokuapp.com/dropdown
Covers: option selection, dynamic content loading, checkbox interaction
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


def test_dropdown_select_option(driver):
    """TC_SEARCH_01: Verify a dropdown option can be selected and reflects correctly."""
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    dropdown.select_by_visible_text("Option 2")
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Option 2"


def test_dropdown_default_state(driver):
    """TC_SEARCH_02: Verify dropdown shows a disabled placeholder by default."""
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    options = dropdown.options
    assert len(options) == 3  # placeholder + 2 real options


def test_checkboxes_toggle(driver):
    """TC_SEARCH_03: Verify checkboxes can be checked and unchecked correctly."""
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    first_checkbox = checkboxes[0]
    initial_state = first_checkbox.is_selected()
    first_checkbox.click()
    assert first_checkbox.is_selected() != initial_state


def test_dynamic_loading_element_appears(driver):
    """TC_SEARCH_04: Verify a dynamically loaded element appears after action (async wait)."""
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    finish_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    assert "Hello World!" in finish_text.text
