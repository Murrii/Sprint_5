# Проверяем:
# вход по кнопке «Войти в аккаунт» на главной,
# вход через кнопку «Личный кабинет»,
# вход через кнопку в форме регистрации,
# вход через кнопку в форме восстановления пароля.

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsRegister, LocatorsLogin, LocatorsMain, LocatorsForgotPassword
from data import LOGIN, PASS

class TestLogin:
    # Проверяем успешную авторизацию по пути Главная -> Войти в аккаунт
    def test_login_from_main_with_valid_log_valid_pass_successful(self, chrome_driver_main):
        chrome_driver_main.find_element(*LocatorsMain.ENTER_TO_ACC_BUTTON).click()

        # ждем, пока прогрузится форма логина
        WebDriverWait(chrome_driver_main, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsLogin.LOGIN_BUTTON))

        # заполняем поля валидными данными для входа
        chrome_driver_main.find_element(*LocatorsLogin.EMAIL_INPUT).send_keys(LOGIN)
        chrome_driver_main.find_element(*LocatorsLogin.PASS_INPUT).send_keys(PASS)
        chrome_driver_main.find_element(*LocatorsLogin.LOGIN_BUTTON).click()

        # ждем, пока загрузится главная страница
        WebDriverWait(chrome_driver_main, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsMain.GET_FOOD_BUTTON))

        # При успешной авторизации появляется кнопка "Оформить заказ", проверяем ее
        assert chrome_driver_main.find_element(*LocatorsMain.GET_FOOD_BUTTON).text == 'Оформить заказ'


    # Проверяем успешную авторизацию по пути Главная -> Личный кабинет
    def test_login_from_main_to_profile_with_valid_log_valid_pass_successful(self, chrome_driver_main):
        chrome_driver_main.find_element(*LocatorsMain.ENTER_TO_PROFILE_BUTTON).click()

        WebDriverWait(chrome_driver_main, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsLogin.LOGIN_BUTTON))

        chrome_driver_main.find_element(*LocatorsLogin.EMAIL_INPUT).send_keys(LOGIN)
        chrome_driver_main.find_element(*LocatorsLogin.PASS_INPUT).send_keys(PASS)
        chrome_driver_main.find_element(*LocatorsLogin.LOGIN_BUTTON).click()

        WebDriverWait(chrome_driver_main, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsMain.GET_FOOD_BUTTON))

        assert chrome_driver_main.find_element(*LocatorsMain.GET_FOOD_BUTTON).text == 'Оформить заказ'

# Проверяем успешную авторизацию по пути Форма восстановления пароля -> Войти
    def test_login_from_registration_form_with_valid_log_valid_pass_successful(self, chrome_driver_register):
        chrome_driver_register.find_element(*LocatorsRegister.LOGIN_BUTTON).click()

        WebDriverWait(chrome_driver_register, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsLogin.LOGIN_BUTTON))

        chrome_driver_register.find_element(*LocatorsLogin.EMAIL_INPUT).send_keys(LOGIN)
        chrome_driver_register.find_element(*LocatorsLogin.PASS_INPUT).send_keys(PASS)
        chrome_driver_register.find_element(*LocatorsLogin.LOGIN_BUTTON).click()

        WebDriverWait(chrome_driver_register, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsMain.GET_FOOD_BUTTON))

        assert chrome_driver_register.find_element(*LocatorsMain.GET_FOOD_BUTTON).text == 'Оформить заказ'

# Проверяем успешную авторизацию по пути Форма восстановления пароля -> Войти в аккаунт
    def test_login_from_forgot_password_form_with_valid_log_valid_pass_successful(self, chrome_driver_forgot_password_page):
        chrome_driver_forgot_password_page.find_element(*LocatorsForgotPassword.LOGIN_BUTTON).click()

        WebDriverWait(chrome_driver_forgot_password_page, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsLogin.LOGIN_BUTTON))

        chrome_driver_forgot_password_page.find_element(*LocatorsLogin.EMAIL_INPUT).send_keys(LOGIN)
        chrome_driver_forgot_password_page.find_element(*LocatorsLogin.PASS_INPUT).send_keys(PASS)
        chrome_driver_forgot_password_page.find_element(*LocatorsLogin.LOGIN_BUTTON).click()

        WebDriverWait(chrome_driver_forgot_password_page, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsMain.GET_FOOD_BUTTON))

        assert chrome_driver_forgot_password_page.find_element(*LocatorsMain.GET_FOOD_BUTTON).text == 'Оформить заказ'
