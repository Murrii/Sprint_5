from selenium.webdriver.common.by import By

class LocatorsRegister:
    NAME_INPUT = (By.XPATH, './/*[text()="Имя"]/parent::div/input')
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/parent::div/input')
    PASS_INPUT = (By.NAME, 'Пароль')
    REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    ERROR_PASS = (By.XPATH, './/*[text()="Некорректный пароль"]')

class LocatorsLogin:
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/parent::div/input')
    PASS_INPUT = (By.NAME, 'Пароль')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')