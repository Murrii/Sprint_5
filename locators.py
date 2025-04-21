from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
class LocatorsRegister:
    NAME_INPUT = (By.XPATH, './/*[text()="Имя"]/parent::div/input') # поле для ввода логина
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/parent::div/input') # поле для ввода емейла
    PASS_INPUT = (By.NAME, 'Пароль') # поле для ввода пароля
    REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]') # кнопка регистрации
    ERROR_PASS = (By.XPATH, './/*[text()="Некорректный пароль"]') # поле с ошибкой ввода пароля
    LOGIN_BUTTON = (By.XPATH, './/*[text()="Войти"]') # кнопка перехода к странице логина

# Локаторы для страницы авторизации
class LocatorsLogin:
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/parent::div/input') # поле для ввода емейла
    PASS_INPUT = (By.NAME, 'Пароль') # поле для ввода пароля
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]') # Кнопка авторизации
    LOGIN_TITLE = (By.XPATH, './/*[text()="Вход"]') # Заголовок экрана авторизации

# Локаторы для главной страницы (конструктора)
class LocatorsMain:
    ENTER_TO_ACC_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]') # кнопка перехода к логину для неавторизированного пользователя
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/*[text()="Личный Кабинет"]') # кнопка перехода к ЛК для авторизированного пользователя
    GET_FOOD_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]') # кнопка оформления заказа для авторизированного пользователя
    ENTER_TO_FEED = (By.XPATH, './/*[text()="Лента Заказов"]') # кнопка перехода к ленте заказов
    MAIN_TITLE = (By.XPATH, './/*[text()="Соберите бургер"]') # Заголовок главной страницы

    # локаторы вкладок конструктора и локаторы элементов, которые выделяются жирным шрифтом для активной вкладки
    MENU_BREAD_FOLDER = (By.XPATH, './/span[text()="Булки"]')
    MENU_BREAD_FOLDER_BOLD_CHECK = (By.XPATH, './/span[text()="Булки"]/parent::div')
    MENU_SOUSE_FOLDER = (By.XPATH, './/span[text()="Соусы"]')
    MENU_SOUSE_FOLDER_BOLD_CHECK = (By.XPATH, './/span[text()="Соусы"]/parent::div')
    MENU_INGREDIENTS_FOLDER = (By.XPATH, './/span[text()="Начинки"]')
    MENU_INGREDIENTS_FOLDER_BOLD_CHECK = (By.XPATH, './/span[text()="Начинки"]/parent::div')

# Локаторы для экрана восстановления пароля
class LocatorsForgotPassword:
    LOGIN_BUTTON = (By.XPATH, './/*[text()="Войти"]') # кнопка возврата к странице авторизации

# Локаторы для Личного кабинета
class LocatorsProfile:
    EXIT_BUTTON = (By.XPATH, './/button[text()="Выход"]') # Кнопка выхода
    GO_TO_MAIN_BUTTON = (By.XPATH, './/*[text()="Конструктор"]') # Кнопка перехода к конструктору
    PROFILE_TITLE = (By.XPATH, './/*[text()="Профиль"]') # заголовок экрана Личный кабинет
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2') # Логотип

# Локаторы для Ленты заказов
class LocatorsFeed:
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/*[text()="Личный Кабинет"]') # Заголовок экрана Лента заказов