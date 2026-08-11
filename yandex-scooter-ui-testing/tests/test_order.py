import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    @allure.feature("Оформление заказа")
    @allure.story("Создание нового заказа")
    @allure.title("Проверка успешного оформления заказа")
    @pytest.mark.parametrize(
        "order_button, name, surname, address, metro, phone, comment",
        [
            (
                "top",
                "Юлиана",
                "Петронина",
                "Москва",
                "Сокольники",
                "+79999999999",
                "Позвонить за час"
            ),
            (
                "bottom",
                "Иван",
                "Иванов",
                "Москва",
                "Черкизовская",
                "+78888888888",
                "Не звонить"
            )
        ]
    )
    def test_create_order_successfully(self,
            driver,
            order_button,
            name,
            surname,
            address,
            metro,
            phone,
            comment
    ):

        with allure.step("Создать объекты страниц"):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step(f"Нажать кнопку Заказать: {order_button}"):
            main_page.click_main_order_button(order_button)

        with allure.step("Заполнить данные заказчика"):
            order_page.fill_customer_info(
                name,
                surname,
                address,
                metro,
                phone
            )

        with allure.step("Заполнить информацию об аренде"):
            order_page.fill_rent_info(comment)

        with allure.step("Нажать кнопку Заказать"):
            order_page.submit_order()

        with allure.step("Подтвердить оформление заказа"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление заказа"):
            assert "Заказ оформлен" in order_page.get_success_header_text()