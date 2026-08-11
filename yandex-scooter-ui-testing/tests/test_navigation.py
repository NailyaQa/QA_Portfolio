import allure
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from data import BASE_URL

class TestNavigation:
    @allure.feature("Навигация")
    @allure.title("Переход на главную страницу по логотипу Самокат")
    def test_click_scooter_logo_opens_main_page(self, driver):

        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Нажать кнопку Заказать"):
            main_page.click_main_order_button("top")

        with allure.step("Нажать на логотип Самокат"):
            main_page.click_scooter_logo()

        with allure.step("Проверить переход на главную страницу"):
            assert driver.current_url == BASE_URL


    @allure.feature("Навигация")
    @allure.title("Открытие Дзена по логотипу Яндекс")
    def test_click_yandex_logo_opens_dzen(self, driver):

        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Нажать на логотип Яндекс"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия новой вкладки"):
            main_page.wait_for_new_tab()

        with allure.step("Переключиться на новую вкладку"):
            main_page.switch_to_last_tab()
            main_page.wait_for_url_contains("dzen")

        with allure.step("Дождаться загрузки Дзена"):
           assert "dzen" in main_page.get_current_url()

        with allure.step("Проверить открытие Дзена"):
            assert "dzen" in driver.current_url