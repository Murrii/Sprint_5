# Sprint_5

Написано 16 тестов, разделенных на 4 файла в зависимости от основной страницы теста:

test_constructor.py включает проверки:
# Проверяем переход к разделу "Булки" - test_go_to_the_bread_successful
# Проверяем переход к разделу "Соусы" - test_go_to_the_souse_successful
# Проверяем переход к разделу "Начинки" - test_go_to_the_ingridients_successful

test_login.py  включает проверки:
# вход по кнопке «Войти в аккаунт» на главной
# вход через кнопку «Личный кабинет»,
# вход через кнопку в форме регистрации,
# вход через кнопку в форме восстановления пароля.

test_profile.py включает проверки:
# Проверяем переход в ЛК с главной страницы - test_go_to_profile_from_main_successful
# Проверяем переход в ЛК со страницы Лента Заказов - test_go_to_profile_from_feed_successful
# Проверяем выход из аккаунта с дальнейшим переходом к экрану логина - test_logout_from_profile_open_login_page
# Проверяем переход из ЛК к конструктору через кнопку "Конструктор" - test_go_from_profile_to_mail_successful
# Проверяем переход из ЛК к конструктору через логотип - test_go_from_profile_to_mail_by_logo_successful

test_register.py  включает проверки:
# Проверяем успешную регистрацию - test_registration_with_valid_login_valid_email_valid_pass_successful
# Проверяем ошибку для некорректного пароля для разных невалидных паролей - test_registration_with_not_valid_pass_error_message  (3 варианта, параметризация)
