# Проверяем переход в ЛК с главной страницы
# Проверяем переход в ЛК со страницы Лента Заказов
# Проверяем выход из аккаунта с дальнейшим переходом к экрану логина
# Проверяем переход из ЛК к конструктору через кнопку "Конструктор"
# Проверяем переход из ЛК к конструктору через логотип

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsMain, LocatorsProfile, LocatorsFeed, LocatorsLogin


class TestProfile:
    # Проверяем переход в ЛК с главной страницы
    # Авторизируемся при помощи фикстуры
    def test_go_to_profile_from_main_successful(self, chrome_driver_login_enter_open_main):
        chrome_driver_login_enter_open_main.find_element(*LocatorsMain.ENTER_TO_PROFILE_BUTTON).click()

        # Уникальный элемент для страницы Профиль - кнопка Выход
        # Ждем загрузку экрана (кликабельность кнопки "Выход") и проверяем заголовок экрана профиля
        WebDriverWait(chrome_driver_login_enter_open_main, 3).until(
            expected_conditions.element_to_be_clickable(LocatorsProfile.EXIT_BUTTON))

        assert chrome_driver_login_enter_open_main.find_element(*LocatorsProfile.PROFILE_TITLE).text == 'Профиль'


    # Проверяем переход в ЛК со страницы Лента Заказов
    # Авторизируемся и переходим на страницу Лента Заказов при помощи фикстуры
    def test_go_to_profile_from_feed_successful(self, chrome_driver_login_enter_open_feed):
        chrome_driver_login_enter_open_feed.find_element(*LocatorsFeed.ENTER_TO_PROFILE_BUTTON).click()

        # Ждем загрузку экрана (кликабельность кнопки "Выход") и проверяем заголовок экрана профиля
        WebDriverWait(chrome_driver_login_enter_open_feed, 3).until(
            expected_conditions.element_to_be_clickable(LocatorsProfile.EXIT_BUTTON))

        assert chrome_driver_login_enter_open_feed.find_element(*LocatorsProfile.PROFILE_TITLE).text == 'Профиль'


    # Проверяем Логаут на странице Личный кабинет
    # Авторизируемся и переходим на страницу Личный кабинет при помощи фикстуры
    def test_logout_from_profile_open_login_page(self, chrome_driver_login_enter_open_profile):
        # Нажимаем на кнопку выхода
        chrome_driver_login_enter_open_profile.find_element(*LocatorsProfile.EXIT_BUTTON).click()

        # Характерная особенность экрана логина - текст "Вход"
        # Ждем загрузку экрана (кликабельность кнопки "Войти") и проверяем заголовок экрана Входа
        WebDriverWait(chrome_driver_login_enter_open_profile, 3).until(
            expected_conditions.element_to_be_clickable(LocatorsLogin.LOGIN_BUTTON))
        assert chrome_driver_login_enter_open_profile.find_element(*LocatorsLogin.LOGIN_TITLE).text == 'Вход'

    # Проверяем переход из ЛК к конструктору через кнопку "Конструктор"
    # Авторизируемся и переходим на страницу Личный кабинет при помощи фикстуры
    def test_go_from_profile_to_mail_successful(self, chrome_driver_login_enter_open_profile):
        # Нажимаем на кнопку перехода к конструктору
        chrome_driver_login_enter_open_profile.find_element(*LocatorsProfile.GO_TO_MAIN_BUTTON).click()
        # Ждем загрузку экрана (кликабельность кнопки "Оформить заказ") и проверяем заголовок экрана Конструктора
        WebDriverWait(chrome_driver_login_enter_open_profile, 3).until(
            expected_conditions.element_to_be_clickable(LocatorsMain.GET_FOOD_BUTTON))

        assert chrome_driver_login_enter_open_profile.find_element(*LocatorsMain.MAIN_TITLE).text == 'Соберите бургер'

    # Проверяем переход из ЛК к конструктору через логотип
    # Авторизируемся и переходим на страницу Личный кабинет при помощи фикстуры
    def test_go_from_profile_to_mail_by_logo_successful(self, chrome_driver_login_enter_open_profile):
        # Нажимаем на логотип
        chrome_driver_login_enter_open_profile.find_element(*LocatorsProfile.LOGO).click()
        # Ждем загрузку экрана (кликабельность кнопки "Оформить заказ") и проверяем заголовок экрана Конструктора
        WebDriverWait(chrome_driver_login_enter_open_profile, 3).until(
            expected_conditions.element_to_be_clickable(LocatorsMain.GET_FOOD_BUTTON))

        assert chrome_driver_login_enter_open_profile.find_element(*LocatorsMain.MAIN_TITLE).text == 'Соберите бургер'