from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from constants import LOGIN_URL


class LoginPage(BasePage):

    def click_register_link(self):
        self.click_element(
            LoginPageLocators.REGISTER_LINK
        )

    def enter_name(self, name):
        self.find_element(
            LoginPageLocators.NAME_FIELD
        ).send_keys(name)

    def enter_register_email(self, email):
        self.find_element(
            LoginPageLocators.REGISTER_EMAIL_FIELD
        ).send_keys(email)

    def enter_register_password(self, password):
        self.find_element(
            LoginPageLocators.REGISTER_PASSWORD_FIELD
        ).send_keys(password)

    def click_register_button(self):
        self.click_element(
            LoginPageLocators.REGISTER_BUTTON
        )

    def register(self, name, email, password):
        self.enter_name(name)
        self.enter_register_email(email)
        self.enter_register_password(password)
        self.click_register_button()

    def enter_login_email(self, email):
        self.find_element(
            LoginPageLocators.LOGIN_EMAIL_FIELD
        ).send_keys(email)

    def enter_login_password(self, password):
        self.find_element(
            LoginPageLocators.LOGIN_PASSWORD_FIELD
        ).send_keys(password)

    

    def login(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.click_login_button()

    def click_login_button(self):
        self.click_element(
            LoginPageLocators.LOGIN_BUTTON
        )

        self.wait.until(
            EC.url_changes(
                LOGIN_URL
            )
    )
        
    def click_login_link(self):
        self.click_element(
        LoginPageLocators.LOGIN_LINK
    )  
        
          