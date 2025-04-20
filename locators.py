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
    LOGIN_TITLE = (By.XPATH, './/*[text()="Вход"]')

class LocatorsMain:
    ENTER_TO_ACC_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/*[text()="Личный Кабинет"]')
    GET_FOOD_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ENTER_TO_FEED = (By.XPATH, './/*[text()="Лента Заказов"]')
    MAIN_TITLE = (By.XPATH, './/*[text()="Соберите бургер"]')

    MENU_BREAD_FOLDER = (By.XPATH, './/span[text()="Булки"]')
    MENU_BREAD_FOLDER_BOLD_CHECK = (By.XPATH, './/span[text()="Булки"]/parent::div')
    MENU_SOUSE_FOLDER = (By.XPATH, './/span[text()="Соусы"]')
    MENU_SOUSE_FOLDER_BOLD_CHECK = (By.XPATH, './/span[text()="Соусы"]/parent::div')
    MENU_INGREDIENTS_FOLDER = (By.XPATH, './/span[text()="Начинки"]')
    MENU_INGREDIENTS_FOLDER_BOLD_CHECK = (By.XPATH, './/span[text()="Начинки"]/parent::div')


class LocatorsForgotPassword:
    LOGIN_BUTTON = (By.XPATH, './/*[text()="Войти"]')

class LocatorsProfile:
    EXIT_BUTTON = (By.XPATH, './/button[text()="Выход"]')
    GO_TO_MAIN_BUTTON = (By.XPATH, './/*[text()="Конструктор"]')
    PROFILE_TITLE = (By.XPATH, './/*[text()="Профиль"]')
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

class LocatorsFeed:
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/*[text()="Личный Кабинет"]')