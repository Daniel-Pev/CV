from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_open_page(driver):
    driver.get('https://daniel-pev.github.io/my_cv/')
    assert driver.current_url == 'https://daniel-pev.github.io/my_cv/'


def test_name(driver):
    driver.get('https://daniel-pev.github.io/my_cv/')
    name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'name'))).text
    assert name.split('\n')[0] == 'Пелевин Даниил'


def test_telegram(driver):
    driver.get('https://daniel-pev.github.io/my_cv/')
    WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.ID, 'telegram')))).click()
    assert driver.current_url == 'https://t.me/Tasteless_one'


def test_github(driver):
    driver.get('https://daniel-pev.github.io/my_cv/')
    WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.ID, 'github')))).click()
    assert driver.current_url == 'https://github.com/Daniel-Pev'


def test_habr(driver):
    driver.get('https://daniel-pev.github.io/my_cv/')
    WebDriverWait(driver, 10).until((EC.presence_of_element_located((By.ID, 'my_habr')))).click()
    assert driver.current_url == 'https://habr.com/ru/users/Tasteless/'
