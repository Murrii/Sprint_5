# Проверяем успешную регистрацию
# Проверяем ошибку для некорректного пароля для разных невалидных паролей

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsRegister, LocatorsLogin

class TestRegistration:
    # Проверяем успешную регистрацию, заодно проверяем заполнение полей валидными значениями
    # Запускаем браузер и генерируем значения для полей при помощи фикстур
    def test_registration_with_valid_login_valid_email_valid_pass_successful(self, chrome_driver_register,
                                                                 random_login, random_pass, random_email):
        WebDriverWait(chrome_driver_register, 5).until(
            expected_conditions.element_to_be_clickable(LocatorsRegister.REGISTER_BUTTON))

        chrome_driver_register.find_element(*LocatorsRegister.NAME_INPUT).send_keys(random_login)
        chrome_driver_register.find_element(*LocatorsRegister.EMAIL_INPUT).send_keys(random_email)
        chrome_driver_register.find_element(*LocatorsRegister.PASS_INPUT).send_keys(random_pass)

        chrome_driver_register.find_element(*LocatorsRegister.REGISTER_BUTTON).click()

        # Ждем загрузку экрана (кликабельность кнопки "Войти") и проверяем заголовок экрана Входа
        WebDriverWait(chrome_driver_register, 2).until(
            expected_conditions.element_to_be_clickable(LocatorsLogin.LOGIN_BUTTON))

        assert chrome_driver_register.find_element(*LocatorsLogin.LOGIN_TITLE).text == 'Вход'



    # Здесь проверяем ошибку при попытке ввести невалидный пароль (меньше 6 символов).
    # Используем параметризацию и проверяем разные невалидные пароли
    # Так как ввод валидых данных мы уже проверили, выносим заполнение валидных полей в фикстуру

    @pytest.mark.parametrize('not_valid_pass', [ 1, '12345', True])
    def test_registration_with_not_valid_pass_error_message(self,
                                                            chrome_driver_register_full_valid_name_email, not_valid_pass):

        chrome_driver_register_full_valid_name_email.find_element(*LocatorsRegister.PASS_INPUT).send_keys(not_valid_pass)
        chrome_driver_register_full_valid_name_email.find_element(*LocatorsRegister.REGISTER_BUTTON).click()

        WebDriverWait(chrome_driver_register_full_valid_name_email, 2).until(
            expected_conditions.visibility_of_element_located(LocatorsRegister.ERROR_PASS))

        error_message = chrome_driver_register_full_valid_name_email.find_element(*LocatorsRegister.ERROR_PASS).text

        assert error_message == 'Некорректный пароль' # проверяем текст ошибки при невалидном пароле
