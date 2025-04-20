# Проверяем переход в ЛК с главной страницы
# Проверяем переход в ЛК со страницы Лента Заказов

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsMain, LocatorsProfile, LocatorsFeed
from data import LOGIN, PASS

class TestProfile:
    # Проверяем переход в ЛК с главной страницы
    # Авторизируемся при помощи фикстуры
    def test_go_to_profile_from_main_successful(self, chrome_driver_login_enter_open_main):
        chrome_driver_login_enter_open_main.find_element(*LocatorsMain.ENTER_TO_PROFILE_BUTTON).click()

        # Уникальный элемент для страницы Профиль - кнопка Выход
        # Ждем, пока страница загрузится и проверяем кнопку выхода
        WebDriverWait(chrome_driver_login_enter_open_main, 3).until(
            expected_conditions.element_to_be_clickable(LocatorsProfile.EXIT_BUTTON))

        assert chrome_driver_login_enter_open_main.find_element(*LocatorsProfile.EXIT_BUTTON).text == 'Выход'

    # Проверяем переход в ЛК со страницы Лента Заказов
    # Авторизируемся и переходим на страницу Лента Заказов при помощи фикстуры
    def test_go_to_profile_from_feed_successful(self, chrome_driver_login_enter_open_feed):
        chrome_driver_login_enter_open_feed.find_element(*LocatorsFeed.ENTER_TO_PROFILE_BUTTON).click()

        WebDriverWait(chrome_driver_login_enter_open_feed, 3).until(
            expected_conditions.element_to_be_clickable(LocatorsProfile.EXIT_BUTTON))

        assert chrome_driver_login_enter_open_feed.find_element(*LocatorsProfile.EXIT_BUTTON).text == 'Выход'
