from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import BASE_URL

import allure


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step("Прокрутить до вопроса FAQ")
    def scroll_to_question(self, index):
        if index == 0:
            locator = MainPageLocators.QUESTION_0
        elif index == 1:
            locator = MainPageLocators.QUESTION_1
        elif index == 2:
            locator = MainPageLocators.QUESTION_2
        elif index == 3:
            locator = MainPageLocators.QUESTION_3
        elif index == 4:
            locator = MainPageLocators.QUESTION_4
        elif index == 5:
            locator = MainPageLocators.QUESTION_5
        elif index == 6:
            locator = MainPageLocators.QUESTION_6
        elif index == 7:
            locator = MainPageLocators.QUESTION_7

        self.scroll_to_element(locator)

        
    @allure.step("Нажать на вопрос FAQ")
    def click_question(self, index):
        if index == 0:
            locator = MainPageLocators.QUESTION_0
        elif index == 1:
            locator = MainPageLocators.QUESTION_1
        elif index == 2:
            locator = MainPageLocators.QUESTION_2
        elif index == 3:
            locator = MainPageLocators.QUESTION_3
        elif index == 4:
            locator = MainPageLocators.QUESTION_4
        elif index == 5:
            locator = MainPageLocators.QUESTION_5
        elif index == 6:
            locator = MainPageLocators.QUESTION_6
        elif index == 7:
            locator = MainPageLocators.QUESTION_7

        self.scroll_and_click(locator)

    

    @allure.step("Нажать кнопку Заказать")
    def click_main_order_button(self, button_type):
        

        if button_type == "top":
            self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

        elif button_type == "bottom":
            self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)


            self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Получить текст ответа FAQ")
    def get_answer_text(self, index):
        if index == 0:
            locator = MainPageLocators.ANSWER_0
        elif index == 1:
            locator = MainPageLocators.ANSWER_1
        elif index == 2:
            locator = MainPageLocators.ANSWER_2
        elif index == 3:
            locator = MainPageLocators.ANSWER_3
        elif index == 4:
            locator = MainPageLocators.ANSWER_4
        elif index == 5:
            locator = MainPageLocators.ANSWER_5
        elif index == 6:
            locator = MainPageLocators.ANSWER_6
        elif index == 7:
            locator = MainPageLocators.ANSWER_7

        return self.get_text(locator)

        
    

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_bottom_order_button(self):
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать логотип Самокат")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
        
    @allure.step("Нажать логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    