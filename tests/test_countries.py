import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json


@pytest.fixture
def driver():
    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_all_countries(driver):
    driver.get("https://www.scrapethissite.com/pages/simple/")

    all_countries = driver.find_elements(By.CLASS_NAME, 'country-name')

    country_names = [country.text for country in all_countries]

    for name in country_names:
        print(name)


def test_all_countries_key_value(driver):
    driver.get("https://www.scrapethissite.com/pages/simple/")

    country_elements = driver.find_elements(By.CLASS_NAME, 'country')

    country_data = {}

    for country in country_elements:
        name = country.find_element(By.CLASS_NAME, 'country-name').text

        capital = country.find_element(By.CLASS_NAME, 'country-capital').text
        population = country.find_element(By.CLASS_NAME, 'country-population').text
        area = country.find_element(By.CLASS_NAME, 'country-area').text

        country_data[name] = [capital, population, area]

    for name, stats in country_data.items():
        print(f"Kraj: {name}, Stolica: {stats[0]}, Populacja: {stats[1]}, Powierzchnia: {stats[2]}")


def test_all_countries_json(driver):
    driver.get("https://www.scrapethissite.com/pages/simple/")

    country_elements = driver.find_elements(By.CLASS_NAME, 'country')

    country_data = {}

    for country in country_elements:
        name = country.find_element(By.CLASS_NAME, 'country-name').text

        capital = country.find_element(By.CLASS_NAME, 'country-capital').text
        population = country.find_element(By.CLASS_NAME, 'country-population').text
        area = country.find_element(By.CLASS_NAME, 'country-area').text

        country_data[name] = {
            "capital": capital,
            "population": population,
            "area": area
        }

    with open('country_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(country_data, json_file, ensure_ascii=False, indent=4)
