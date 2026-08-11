import allure

from pages.main_page import MainPage

class TestConstructor:


    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(
        self,
        driver,
        authorized_user
    ):
        main_page = MainPage(driver)

        with allure.step("Нажать на ингредиент «Филе Люминесцентного тетраодонтимформа»"):
            main_page.click_filling()

        with allure.step(
            "Проверить, что открылось модальное окно "
            "с деталями ингредиента"
        ):
            assert main_page.is_ingredient_modal_open()


    @allure.title("Закрытие деталей ингредиента")
    def test_close_ingredient_details(
        self,
        driver,
        authorized_user
    ):
        main_page = MainPage(driver)

        with allure.step("Открыть детали ингредиента"):
            main_page.click_filling()

        with allure.step("Закрыть модальное окно ингредиента"):
            main_page.close_ingredient_modal()

        with allure.step(
            "Проверить, что модальное окно закрылось"
        ):
            assert main_page.is_ingredient_modal_closed()


    @allure.title(
        "Счётчик ингредиента увеличивается "
        "после добавления ингредиента"
    )
    def test_ingredient_counter_increases_after_adding(
        self,
        driver,
        authorized_user
    ):
        main_page = MainPage(driver)

        with allure.step(
            "Запомнить исходное значение счётчика ингредиента"
        ):
            old_count = (
                main_page.get_ingredient_counter()
            )

        with allure.step(
            "Добавить ингредиент в заказ"
        ):
            main_page.add_ingredient()

        

        with allure.step(
            "Проверить увеличение счётчика ингредиента"
        ):
            new_count = (
                main_page.get_ingredient_counter()
            )

            assert new_count == old_count + 1


