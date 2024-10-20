import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_invalid_username(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login = driver.find_element(By.ID, "username")
    login.send_keys('invalid_user')

    password = driver.find_element(By.ID, "password")
    password.send_keys('Password123')

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "#error")
    assert error_message.text == 'Your username is invalid!', "Błędny komunikat o niepoprawnej nazwie użytkownika"


def test_invalid_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login = driver.find_element(By.ID, "username")
    login.send_keys('student')

    password = driver.find_element(By.ID, "password")
    password.send_keys('invalid_password')

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "#error")
    assert error_message.text == 'Your password is invalid!', "Błędny komunikat o niepoprawnym haśle"

