import pytest
from data import URL_LOGIN, URL_MAIN, URL_REGISTER, URL_FEED, URL_FORGOT_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import randint
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsRegister

@pytest.fixture
def chrome_driver_login_page():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_LOGIN)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture
def chrome_driver_main():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_MAIN)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture
def chrome_driver_feed():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_FEED)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture
def chrome_driver_register():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_REGISTER)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture
def chrome_driver_forgot_password_page():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_FORGOT_PASSWORD)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture
def random_login():
    login = str(randint(100, 999)) + ' удава'
    return login

@pytest.fixture
def random_pass():
    password = str(randint(100, 999)) + 'abc'
    return password

@pytest.fixture
def random_email():
    email = 'karinatrofimova20' + str(randint(100, 999)) + '@yandex.ru'
    return email

@pytest.fixture
def chrome_driver_register_full_valid_name_email(chrome_driver_register, random_email, random_login):
    WebDriverWait(chrome_driver_register, 3).until(
        expected_conditions.element_to_be_clickable(LocatorsRegister.REGISTER_BUTTON))

    chrome_driver_register.find_element(*LocatorsRegister.NAME_INPUT).send_keys(random_login)
    chrome_driver_register.find_element(*LocatorsRegister.EMAIL_INPUT).send_keys(random_email)

    yield chrome_driver_register

    chrome_driver_register.quit()
