"""
Test Suite: Form Validation & File Upload
Target: https://the-internet.herokuapp.com
Covers: form input validation, alert handling, file upload flow
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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


def test_javascript_alert_accept(driver):
    """TC_FORM_01: Verify a JS alert can be triggered and accepted."""
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    assert alert.text == "I am a JS Alert"
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert "You successfully clicked an alert" in result.text


def test_javascript_confirm_dismiss(driver):
    """TC_FORM_02: Verify a JS confirm dialog can be dismissed (Cancel)."""
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.dismiss()

    result = driver.find_element(By.ID, "result")
    assert "You clicked: Cancel" in result.text


def test_add_remove_elements(driver):
    """TC_FORM_03: Verify elements can be dynamically added and removed."""
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

    add_button.click()
    add_button.click()
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    assert len(delete_buttons) == 2

    delete_buttons[0].click()
    remaining = driver.find_elements(By.CLASS_NAME, "added-manually")
    assert len(remaining) == 1


def test_form_authentication_page_title(driver):
    """TC_FORM_04: Sanity check — verify correct page loads with expected title/header."""
    driver.get("https://the-internet.herokuapp.com/login")
    header = driver.find_element(By.TAG_NAME, "h2")
    assert header.text == "Login Page"
