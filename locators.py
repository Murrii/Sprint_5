from selenium.webdriver.common.by import By

class LocatorsRegister:
    NAME_INPUT = (By.XPATH, './/*[text()="Имя"]/parent::div/input')
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/parent::div/input')
    PASS_INPUT = (By.NAME, 'Пароль')
    REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    ERROR_PASS = (By.XPATH, './/*[text()="Некорректный пароль"]')
    LOGIN_BUTTON = (By.XPATH, './/*[text()="Войти"]')

class LocatorsLogin:
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/parent::div/input')
    PASS_INPUT = (By.NAME, 'Пароль')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')

class LocatorsMain:
    ENTER_TO_ACC_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/*[text()="Личный Кабинет"]')
    GET_FOOD_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ENTER_TO_FEED = (By.XPATH, './/*[text()="Лента Заказов"]')

class LocatorsForgotPassword:
    LOGIN_BUTTON = (By.XPATH, './/*[text()="Войти"]')

class LocatorsProfile:
    EXIT_BUTTON = (By.XPATH, './/button[text()="Выход"]')

class LocatorsFeed:
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/*[text()="Личный Кабинет"]')