# Проверяем переход к разделу "Булки"
# Проверяем переход к разделу "Соусы"
# Проверяем переход к разделу "Начинки"

from locators import LocatorsMain


class TestConstructor:
    # Проверяем переход к разделу "Булки"
    def test_go_to_the_bread_successful(self, chrome_driver_login_enter_open_main):

        # переходим на какую-либо другую вкладку, чтобы снять выделение с вкладки "Булки"
        chrome_driver_login_enter_open_main.find_element(*LocatorsMain.MENU_INGREDIENTS_FOLDER).click()
        # возвращаемся к "Булкам"
        chrome_driver_login_enter_open_main.find_element(*LocatorsMain.MENU_BREAD_FOLDER).click()
        # проверяем, что выбрана вкладка "булки" (вкладка выделена жирным)
        assert (chrome_driver_login_enter_open_main.find_element(
            *LocatorsMain.MENU_BREAD_FOLDER_BOLD_CHECK).get_attribute('class') ==
                'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')

    # Проверяем переход к разделу "Соусы"
    def test_go_to_the_souse_successful(self, chrome_driver_login_enter_open_main):
        # Переходим к разделу Соусы
        chrome_driver_login_enter_open_main.find_element(*LocatorsMain.MENU_SOUSE_FOLDER).click()
        # проверяем, что выбрана вкладка "Соусы" (вкладка выделена жирным)
        assert (chrome_driver_login_enter_open_main.find_element(
            *LocatorsMain.MENU_SOUSE_FOLDER_BOLD_CHECK).get_attribute('class') ==
             'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')


    # Проверяем переход к разделу "Начинки"
    def test_go_to_the_ingridients_successful(self, chrome_driver_login_enter_open_main):
        # Переходим к разделу Начинки
        chrome_driver_login_enter_open_main.find_element(*LocatorsMain.MENU_INGREDIENTS_FOLDER).click()
        # проверяем, что выбрана вкладка "Начинки" (вкладка выделена жирным)
        assert (chrome_driver_login_enter_open_main.find_element(
            *LocatorsMain.MENU_INGREDIENTS_FOLDER_BOLD_CHECK).get_attribute('class') ==
             'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')
