
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators



class MainPage(BasePage):

    def click_account(self):
        self.click_element(
            MainPageLocators.ACCOUNT_BUTTON
        )

    def click_constructor(self):
        self.click_element(
            MainPageLocators.CONSTRUCTOR_BUTTON
        )

    def click_order_feed(self):
        self.click_element(
            MainPageLocators.ORDER_FEED_BUTTON
        )

    def click_bun(self):
        self.click_element(
            MainPageLocators.BUN_INGREDIENT
        )

    def click_sauce(self):
        self.click_element(
            MainPageLocators.SAUCE_INGREDIENT
        )

    def click_filling(self):
        self.click_element(
            MainPageLocators.FILLING_INGREDIENT
        )

    def close_ingredient_modal(self):
        self.click_element(
            MainPageLocators.CLOSE_MODAL_BUTTON
        )

    def get_ingredient_counter(self):
        return int(
            self.get_text(
                MainPageLocators.INGREDIENT_COUNTER
            )
        )

    def click_order_button(self):
        self.click_element(
            MainPageLocators.ORDER_BUTTON
        )

    def get_constructor_title(self):
        return self.get_text(
            MainPageLocators.CONSTRUCTOR_TITLE
        )

    def get_order_number(self):
        return self.get_text(
            MainPageLocators.ORDER_NUMBER
        )
    def close_order_modal(self):
        self.remove_modal()
        
    def add_bun(self):
        self.drag_and_drop_js(
            MainPageLocators.BUN_INGREDIENT,
            MainPageLocators.SELECTED_INGREDIENTS
        )


    def add_ingredient(self):
        self.drag_and_drop_js(
            MainPageLocators.FILLING_INGREDIENT,
            MainPageLocators.SELECTED_INGREDIENTS
        )

    

   

    def wait_for_order_number(self):
        def get_real_order_number(_):
            order_number = self.get_order_number()

            

            if order_number and order_number != "9999":
                return order_number

            return False

        return self.wait.until(get_real_order_number)  

    def is_ingredient_modal_open(self):
        return self.find_element(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        ).is_displayed()
    
    def is_ingredient_modal_closed(self):
        return self.wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.INGREDIENT_MODAL
            )
        )
    
    def get_selected_ingredients(self):
        return self.get_text(
            MainPageLocators.SELECTED_INGREDIENTS
        )

    def is_ingredient_modal_closed(self):
        self.wait_for_invisibility(
            MainPageLocators.INGREDIENT_MODAL
        )

   

    def close_ingredient_modal(self):
        self.click_element(
            MainPageLocators.CLOSE_MODAL_BUTTON
        )

    def close_ingredient_modal(self):
        self.click_element(
            MainPageLocators.CLOSE_INGREDIENT_MODAL_BUTTON
        )


    def is_ingredient_modal_closed(self):
        return self.wait_for_invisibility(
            MainPageLocators.INGREDIENT_MODAL
        )
    def is_ingredient_modal_closed(self):
            return self.wait.until(
                EC.invisibility_of_element_located(
                    MainPageLocators.INGREDIENT_MODAL
                )
            )
    
   