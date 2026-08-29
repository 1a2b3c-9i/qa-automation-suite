"""
Test Suite: Login Functionality
Target: https://the-internet.herokuapp.com/login
Covers: valid login, invalid login, empty field validation
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "https://the-internet.herokuapp.com/login"


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


def test_login_valid_credentials(driver):
    """TC_LOGIN_01: Verify login succeeds with valid credentials."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )
    assert "You logged into a secure area" in success_message.text


def test_login_invalid_credentials(driver):
    """TC_LOGIN_02: Verify login fails with invalid credentials and shows an error."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
    )
    assert "Your username is invalid" in error_message.text
    assert "login" in driver.current_url  # user should NOT be redirected


def test_login_empty_fields(driver):
    """TC_LOGIN_03: Verify submitting empty fields shows a validation error."""
    driver.get(BASE_URL)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
    )
    assert error_message.is_displayed()


def test_logout_flow(driver):
    """TC_LOGIN_04: Verify a logged-in user can log out successfully."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    logout_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/logout']"))
    )
    logout_button.click()

    login_form = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    assert login_form.is_displayed()
