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


def test_successful_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login = driver.find_element(By.ID, "username")
    login.send_keys('student')

    password = driver.find_element(By.ID, "password")
    password.send_keys('Password123')

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    login_alert = driver.find_element(By.CSS_SELECTOR, ".post-title")
    assert login_alert.text == 'Logged In Successfully', "Błędny komunikat"

    assert driver.current_url == 'https://practicetestautomation.com/logged-in-successfully/', "Błędny URL"

    logout_button = driver.find_element(By.CSS_SELECTOR,
                                        ".wp-block-button__link.has-text-color.has-background.has-very-dark-gray"
                                        "-background-color")
    assert logout_button.text == 'Log out', "Błędny tekst przycisku"
