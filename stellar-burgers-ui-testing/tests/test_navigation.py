import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestNavigation:

    @allure.title(
        "Переход в раздел «Конструктор»"
    )
    def test_go_to_constructor(
        self,
        driver,
        authorized_user
    ):
        main_page = MainPage(driver)

        with allure.step(
            "Перейти в раздел «Лента заказов»"
        ):
            main_page.click_order_feed()

        with allure.step(
            "Перейти в раздел «Конструктор»"
        ):
            main_page.click_constructor()

        with allure.step(
            "Проверить, что открыт раздел «Конструктор»"
        ):
            assert (
                main_page.get_constructor_title()
                == "Соберите бургер"
            )

    @allure.title(
        "Переход в раздел «Лента заказов»"
    )
    def test_go_to_order_feed(
        self,
        driver,
        authorized_user
    ):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step(
            "Перейти в раздел «Лента заказов»"
        ):
            main_page.click_order_feed()

        with allure.step(
            "Проверить, что открыта «Лента заказов»"
        ):
            total_orders = (
                order_feed_page.get_total_orders_count()
            )

            assert isinstance(
                total_orders,
                int
            )