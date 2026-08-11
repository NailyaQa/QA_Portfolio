import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage






class TestOrderFeed:

    @allure.title(
        "Счётчик «Выполнено за всё время» "
        "увеличивается после создания нового заказа"
    )
    def test_total_orders_count_increases_after_new_order(
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
            "Запомнить текущее количество выполненных заказов"
        ):
            old_count = (
                order_feed_page.get_total_orders_count()
            )

        with allure.step(
            "Перейти в «Конструктор»"
        ):
            main_page.click_constructor()

        with allure.step(
            "Добавить булочку в заказ"
        ):
            main_page.add_bun()

        with allure.step("Добавить начинку в заказ"):
            main_page.add_ingredient()

        with allure.step(
            "Нажать кнопку «Оформить заказ»"
        ):
            main_page.click_order_button()

        with allure.step(
            "Дождаться получения номера созданного заказа"
        ):
            order_number = (
                main_page.wait_for_order_number()
        )

        

        with allure.step(
            "Закрыть модальное окно заказа"
        ):
            main_page.close_order_modal()

        with allure.step(
            "Перейти в раздел «Лента заказов»"
        ):
            main_page.click_order_feed()

        with allure.step(
            "Дождаться увеличения счётчика «Выполнено за всё время»"
        ):
            order_feed_page.wait_for_total_orders_count_increase(
                old_count
            )

        with allure.step(
            "Получить новое количество выполненных заказов"
        ):
            new_count = (
                order_feed_page.get_total_orders_count()
            )
        
        with allure.step(
            "Проверить увеличение счётчика"
        ):
            assert new_count > old_count

    @allure.title(
"Счётчик «Выполнено за сегодня» увеличивается "
"после создания нового заказа"
)
    def test_today_orders_count_increases_after_new_order(
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
            "Запомнить текущее количество выполненных заказов за сегодня"
        ):
            old_count = (
                order_feed_page.get_today_orders_count()
            )

        with allure.step(
            "Перейти в «Конструктор»"
        ):
            main_page.click_constructor()

        with allure.step(
            "Добавить булочку в заказ"
        ):
            main_page.add_bun()

        with allure.step(
            "Добавить начинку в заказ"
        ):
            main_page.add_ingredient()

        with allure.step(
            "Оформить заказ"
        ):
            main_page.click_order_button()

        with allure.step(
            "Получить номер созданного заказа"
        ):
            order_number = (
                main_page.get_order_number()
            )
        
        with allure.step(
            "Закрыть модальное окно заказа"
        ):
            main_page.close_order_modal()

        with allure.step(
            "Перейти в раздел «Лента заказов»"
        ):
            main_page.click_order_feed()

        with allure.step(
            "Дождаться увеличения счётчика выполненных заказов за сегодня"
        ):
            order_feed_page.wait_for_today_orders_count_increase(
                old_count
            )

        with allure.step(
            "Получить новое количество выполненных заказов за сегодня"
        ):
            new_count = (
                order_feed_page.get_today_orders_count()
            )

        
        


        with allure.step(
                "Проверить увеличение счётчика"
            ):
                assert new_count > old_count


    @allure.title(
        "Новый заказ появляется в разделе «В работе»"
    )
    def test_new_order_appears_in_orders_in_progress(
        self,
        driver,
        authorized_user
    ):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Перейти в «Конструктор»"):
            main_page.click_constructor()

        with allure.step("Добавить булочку в заказ"):
            main_page.add_bun()

        with allure.step("Добавить начинку в заказ"):
            main_page.add_ingredient()

        with allure.step("Оформить заказ"):
            main_page.click_order_button()

        with allure.step(
            "Дождаться получения номера созданного заказа"
        ):
            order_number = (
                main_page.wait_for_order_number()
            )


        with allure.step("Закрыть модальное окно заказа"):
            main_page.close_order_modal()

        with allure.step("Перейти в «Ленту заказов»"):
            main_page.click_order_feed()
        
        with allure.step(
            "Дождаться появления заказа в разделе «В работе»"
        ):
            order_feed_page.wait_for_order_in_progress(
                order_number
            )