import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_save_club_data(driver):
    driver.get("http://www.scrapethissite.com/pages/forms/")

    search_field = driver.find_element(By.ID, 'q')
    search_button = driver.find_element(By.CSS_SELECTOR, "input[value='Search']")

    search_field.send_keys('pa')
    search_button.click()

    items_per_page = driver.find_element(By.ID, 'per_page')
    select = Select(items_per_page)
    select.select_by_value('50')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.team')))

    clubs_data = []
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr.team')

    for row in rows:
        team_name = row.find_element(By.CSS_SELECTOR, '.name').text.strip()
        year = row.find_element(By.CSS_SELECTOR, '.year').text.strip()
        wins = row.find_element(By.CSS_SELECTOR, '.wins').text.strip()
        losses = row.find_element(By.CSS_SELECTOR, '.losses').text.strip()
        win_percentage = row.find_element(By.CSS_SELECTOR, '.pct').text.strip()

        clubs_data.append([team_name, year, wins, losses, win_percentage])

    with open('clubs_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Team Name', 'Year', 'Wins', 'Losses', 'Win %'])
        for club in clubs_data:
            writer.writerow(club)

    print("Dane zostały zapisane do pliku 'clubs_data.csv'.")
