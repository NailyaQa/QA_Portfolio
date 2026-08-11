from pages.base_page import BasePage

from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage(BasePage):

    @allure.step("Заполнить данные заказчика")
    def fill_customer_info(
            self,
            name,
            surname,
            address,
            metro,
            phone
    ):
        self.fill_input(OrderPageLocators.NAME_FIELD, name)

        self.fill_input(OrderPageLocators.SURNAME_FIELD, surname)

        self.fill_input(OrderPageLocators.ADDRESS_FIELD, address)

        self.click_element(
            OrderPageLocators.METRO_FIELD
        )

        self.click_element(OrderPageLocators.metro_station(metro))

        self.fill_input(OrderPageLocators.PHONE_FIELD, phone)

        self.click_element(
            OrderPageLocators.NEXT_BUTTON
        )

    @allure.step("Заполнить данные аренды")
    def fill_rent_info(self, comment):
        self.click_element(
            OrderPageLocators.DATE_FIELD
        )

        self.click_element(
            OrderPageLocators.ACTIVE_DAY
        )

        self.click_element(
            OrderPageLocators.RENTAL_PERIOD_FIELD
        )

        self.click_element(
            OrderPageLocators.THREE_DAYS_OPTION
        )

        self.click_element(
            OrderPageLocators.GREY_CHECKBOX
        )

        self.fill_input(OrderPageLocators.COMMENT_FIELD,comment)

    @allure.step("Нажать кнопку Заказать")
    def submit_order(self):
        self.click_element(
        OrderPageLocators.ORDER_BUTTON
    )
        
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_and_click(OrderPageLocators.CONFIRM_YES_BUTTON)
    
    @allure.step("Получить текст успешного оформления заказа")
    def get_success_header_text(self):
        return self.get_text(
            OrderPageLocators.SUCCESS_MODAL_HEADER
        )
    
    
   
    