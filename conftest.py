import pytest
from data import URL_LOGIN, URL_MAIN, URL_REGISTER, URL_FEED, URL_FORGOT_PASSWORD, PASS, LOGIN
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import randint
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsRegister, LocatorsLogin, LocatorsMain, LocatorsProfile

# Открываем экран авторизации
@pytest.fixture
def chrome_driver_login_page():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_LOGIN)

    yield chrome_driver


    chrome_driver.quit()

# Открываем экран авторизации и авторизируемся
# Ждем, пока прогрузятся элементы экрана, затем передаем в тест
@pytest.fixture
def chrome_driver_login_enter_open_main(chrome_driver_login_page):
    chrome_driver_login_page.find_element(*LocatorsLogin.EMAIL_INPUT).send_keys(LOGIN)
    chrome_driver_login_page.find_element(*LocatorsLogin.PASS_INPUT).send_keys(PASS)
    chrome_driver_login_page.find_element(*LocatorsLogin.LOGIN_BUTTON).click()

    WebDriverWait(chrome_driver_login_page, 3).until(
        expected_conditions.element_to_be_clickable(LocatorsMain.GET_FOOD_BUTTON))

    yield chrome_driver_login_page

    chrome_driver_login_page.quit()

# Авторизируемся и переходим к экрану Лента Заказов
@pytest.fixture
def chrome_driver_login_enter_open_feed(chrome_driver_login_enter_open_main):
    chrome_driver_login_enter_open_main.find_element(*LocatorsMain.ENTER_TO_FEED).click()

    yield chrome_driver_login_enter_open_main

    chrome_driver_login_enter_open_main.quit()

# Авторизируемся и переходим к экрану Личный кабинет.
# Ждем, пока прогрузятся элементы экрана, затем передаем в тест
@pytest.fixture
def chrome_driver_login_enter_open_profile(chrome_driver_login_enter_open_main):
    chrome_driver_login_enter_open_main.find_element(*LocatorsMain.ENTER_TO_PROFILE_BUTTON).click()
    WebDriverWait(chrome_driver_login_enter_open_main, 3).until(
        expected_conditions.element_to_be_clickable(LocatorsProfile.EXIT_BUTTON))

    yield chrome_driver_login_enter_open_main

    chrome_driver_login_enter_open_main.quit()

# Открываем экран Главная без авторизации
@pytest.fixture
def chrome_driver_main():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_MAIN)

    yield chrome_driver

    chrome_driver.quit()

# Открываем экран Лента Заказов без авторизации
@pytest.fixture
def chrome_driver_feed():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_FEED)

    yield chrome_driver

    chrome_driver.quit()

# Открываем экран Регистрация
@pytest.fixture
def chrome_driver_register():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_REGISTER)

    yield chrome_driver

    chrome_driver.quit()

# Открываем экран Восстановление пароля
@pytest.fixture
def chrome_driver_forgot_password_page():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options)
    chrome_driver.get(URL_FORGOT_PASSWORD)

    yield chrome_driver

    chrome_driver.quit()

# генераторы логина, пароля, email
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

# Открываем страницу регистрации и заполняем поля Логин и Email
@pytest.fixture
def chrome_driver_register_full_valid_name_email(chrome_driver_register, random_email, random_login):
    WebDriverWait(chrome_driver_register, 3).until(
        expected_conditions.element_to_be_clickable(LocatorsRegister.REGISTER_BUTTON))

    chrome_driver_register.find_element(*LocatorsRegister.NAME_INPUT).send_keys(random_login)
    chrome_driver_register.find_element(*LocatorsRegister.EMAIL_INPUT).send_keys(random_email)

    yield chrome_driver_register

    chrome_driver_register.quit()
